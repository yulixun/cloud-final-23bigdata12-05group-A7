const out = document.getElementById("out");
const dbPanel = document.getElementById("dbPanel");
const dbTable = document.getElementById("dbTable");
const dbMeta = document.getElementById("dbMeta");

function showRaw(v) {
  out.textContent = typeof v === "string" ? v : JSON.stringify(v, null, 2);
}

function setHidden(el, hidden) {
  el.classList.toggle("hidden", hidden);
}

function escapeHtml(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

// 尝试从各种后端返回格式里“提取表格行”
// 支持：数组；或对象里含 rows/data/latest/items/records/result 等数组字段
function extractRows(payload) {
  if (Array.isArray(payload)) return payload;

  if (payload && typeof payload === "object") {
    const keys = ["rows", "data", "latest", "items", "records", "result", "list"];
    for (const k of keys) {
      if (Array.isArray(payload[k])) return payload[k];
    }
  }
  return null;
}

function renderTable(rows) {
  if (!rows || rows.length === 0) {
    dbTable.innerHTML = "<tr><td class='muted'>返回为空（0 条记录）</td></tr>";
    dbMeta.textContent = "0 条";
    return;
  }

  // rows 可以是对象数组，也可以是基础类型数组
  const isObj = typeof rows[0] === "object" && rows[0] !== null && !Array.isArray(rows[0]);

  if (!isObj) {
    dbTable.innerHTML = `
      <thead><tr><th>#</th><th>value</th></tr></thead>
      <tbody>
        ${rows.map((v, i) => `<tr><td>${i + 1}</td><td>${escapeHtml(v)}</td></tr>`).join("")}
      </tbody>
    `;
    dbMeta.textContent = `${rows.length} 条（非对象数组）`;
    return;
  }

  // 动态表头：取所有行的字段并去重
  const cols = Array.from(
    rows.reduce((set, r) => {
      Object.keys(r).forEach(k => set.add(k));
      return set;
    }, new Set())
  );

  const thead = `<thead><tr>${cols.map(c => `<th>${escapeHtml(c)}</th>`).join("")}</tr></thead>`;
  const tbody = `<tbody>${
    rows.map(r => `<tr>${cols.map(c => `<td>${escapeHtml(r[c] ?? "")}</td>`).join("")}</tr>`).join("")
  }</tbody>`;

  dbTable.innerHTML = thead + tbody;
  dbMeta.textContent = `${rows.length} 条记录，字段：${cols.join(", ")}`;
}

async function callApi(path) {
  const res = await fetch(path, { method: "GET" });
  const text = await res.text();
  try { return JSON.parse(text); } catch { return text; }
}

document.getElementById("btnHealth").addEventListener("click", async () => {
  showRaw("请求中...");
  setHidden(dbPanel, true);
  try {
    const data = await callApi("/api/health");
    showRaw(data);
  } catch (e) {
    showRaw("失败：" + e.message);
  }
});

document.getElementById("btnDb").addEventListener("click", async () => {
  showRaw("请求中...");
  try {
    const data = await callApi("/api/db");
    showRaw(data);

    const rows = extractRows(data);
    if (rows) {
      setHidden(dbPanel, false);
      renderTable(rows);
    } else {
      // 不是数组结构也没关系：依旧算“调用成功”，只是无法表格化
      setHidden(dbPanel, false);
      dbMeta.textContent = "返回不是数组结构（已显示原始 JSON）";
      dbTable.innerHTML = "<tr><td class='muted'>未检测到可表格化的 rows/data/latest/items… 数组字段</td></tr>";
    }
  } catch (e) {
    setHidden(dbPanel, true);
    showRaw("失败：" + e.message);
  }
});

document.getElementById("btnClear").addEventListener("click", () => {
  showRaw("等待操作…");
  setHidden(dbPanel, true);
  dbTable.innerHTML = "";
  dbMeta.textContent = "—";
});