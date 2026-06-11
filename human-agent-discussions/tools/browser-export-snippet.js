/*
 * Claude conversation exporter — browser console snippet.
 *
 * Downloads all conversations of the logged-in claude.ai account as a
 * conversations.json file compatible with archive_sessions.py.
 *
 * Usage (per account, ~1 min):
 *   1. Log in to claude.ai with the account you want to export.
 *   2. Open DevTools (F12) → Console tab.
 *   3. Paste this whole file and press Enter.
 *      (If the browser warns about pasting, type "allow pasting" first —
 *      that warning exists because pasted code runs with your session.)
 *   4. Wait for the progress log; a conversations.json download starts
 *      automatically when done.
 *   5. Drop the file into human-agent-discussions/_incoming/<account>/.
 *
 * Notes:
 *   - Uses claude.ai's internal (unofficial, undocumented) endpoints from
 *     inside your own logged-in tab; nothing is sent anywhere else.
 *   - May break if Anthropic changes the endpoints. The official
 *     Settings → Privacy → Export data flow is the fallback.
 *   - Set SINCE to skip old conversations, e.g. "2026-01-01".
 */
(async () => {
  const SINCE = null; // e.g. "2026-01-01" to skip conversations older than this
  const DELAY_MS = 300; // politeness delay between conversation fetches

  const headers = { accept: "application/json" };
  const get = async (path) => {
    const r = await fetch(path, { credentials: "include", headers });
    if (!r.ok) throw new Error(`GET ${path} -> HTTP ${r.status}`);
    return r.json();
  };

  const orgs = await get("/api/organizations");
  const org =
    orgs.find((o) => (o.capabilities || []).includes("chat")) || orgs[0];
  if (!org) throw new Error("no organization found — are you logged in?");
  console.log(`org: ${org.name || org.uuid}`);

  // List conversations (paginated; tolerate full-array responses).
  let list = [];
  for (let offset = 0; ; ) {
    let page = await get(
      `/api/organizations/${org.uuid}/chat_conversations?limit=100&offset=${offset}`
    );
    if (!Array.isArray(page)) page = page.conversations || page.data || [];
    const known = new Set(list.map((c) => c.uuid));
    const fresh = page.filter((c) => !known.has(c.uuid));
    list = list.concat(fresh);
    if (page.length < 100 || fresh.length === 0) break;
    offset += page.length;
  }
  if (SINCE) list = list.filter((c) => (c.updated_at || c.created_at || "") >= SINCE);
  console.log(`${list.length} conversation(s) to fetch`);

  const out = [];
  for (let i = 0; i < list.length; i++) {
    const c = list[i];
    try {
      const d = await get(
        `/api/organizations/${org.uuid}/chat_conversations/${c.uuid}` +
          `?tree=True&rendering_mode=messages&render_all_tools=true`
      );
      out.push(d);
      console.log(`${i + 1}/${list.length}  ${d.name || c.uuid}`);
    } catch (e) {
      console.warn(`${i + 1}/${list.length}  FAILED ${c.uuid}: ${e.message}`);
    }
    await new Promise((s) => setTimeout(s, DELAY_MS));
  }

  const blob = new Blob([JSON.stringify(out)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "conversations.json";
  a.click();
  console.log(
    `done: ${out.length} conversation(s) exported -> conversations.json\n` +
      "next: drop it into human-agent-discussions/_incoming/<account>/ and run\n" +
      "  python3 human-agent-discussions/tools/archive_sessions.py"
  );
})();
