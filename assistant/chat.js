// QOU Chat — Claude-like streaming chat panel with active feedback
// Integrates with /api/chat SSE endpoint

(function () {
  "use strict";

  // ── Helpers ──────────────────────────────────────────────
  const $ = (s, p) => (p || document).querySelector(s);
  const h = (tag, cls, html) => {
    const el = document.createElement(tag);
    if (cls) el.className = cls;
    if (html != null) el.innerHTML = html;
    return el;
  };
  function esc(s) {
    if (s == null) return "";
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  // ── State ───────────────────────────────────────────────
  let messages = [];      // { role, content, suggestions? }[]
  let isStreaming = false;
  let abortController = null;
  let currentPaperId = null;
  let chatOpen = false;

  // Detect paper context from hash
  function getPaperContext() {
    const hash = location.hash || "#/";
    const parts = hash.slice(2).split("/").filter(Boolean);
    if (parts[0] === "paper" && parts[1]) {
      currentPaperId = parts[1];
      return { paperId: parts[1] };
    }
    return {};
  }

  // ── Markdown → HTML (chat-optimized, handles partial content) ──
  function chatMdToHtml(md) {
    if (!md) return "";
    let out = md;

    // Strip [suggestions]: line (handled separately)
    out = out.replace(/\[suggestions\]:.*$/m, "").trim();

    // Display math $$...$$
    out = out.replace(/\$\$([\s\S]*?)\$\$/g, (_, tex) =>
      `<span class="chat-katex-display" data-tex="${esc(tex.trim()).replace(/'/g, "&#39;")}"></span>`);
    // Inline math $...$
    out = out.replace(/\$([^\n$]+?)\$/g, (_, tex) =>
      `<span class="chat-katex-inline" data-tex="${esc(tex.trim()).replace(/'/g, "&#39;")}"></span>`);
    // Fenced code blocks
    out = out.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) =>
      `<pre class="chat-code"><code>${esc(code)}</code></pre>`);
    // Inline code
    out = out.replace(/`([^`\n]+)`/g, '<code class="chat-inline-code">$1</code>');
    // Bold
    out = out.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    // Italic
    out = out.replace(/\*(.+?)\*/g, "<em>$1</em>");
    // Links
    out = out.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    // Lists
    out = out.replace(/^[-*] (.+)$/gm, '<li>$1</li>');
    out = out.replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>');
    // Numbered lists
    out = out.replace(/^\d+\. (.+)$/gm, '<li>$1</li>');
    // Headers (in chat, keep them subtle)
    out = out.replace(/^### (.+)$/gm, '<div class="chat-h3">$1</div>');
    out = out.replace(/^## (.+)$/gm, '<div class="chat-h2">$1</div>');
    // Paragraphs
    out = out.replace(/\n{2,}/g, "</p><p>");
    out = "<p>" + out + "</p>";
    // Clean up empty paragraphs
    out = out.replace(/<p>\s*<\/p>/g, "");
    return out;
  }

  // Extract suggestions from response
  function extractSuggestions(text) {
    const match = text.match(/\[suggestions\]:\s*(.+)$/m);
    if (!match) return [];
    return match[1].split("|").map(s => s.trim()).filter(Boolean);
  }

  // Render KaTeX in a container
  function renderChatMath(container) {
    if (!window.katex) return;
    container.querySelectorAll(".chat-katex-display").forEach(el => {
      if (el.dataset.rendered) return;
      try {
        katex.render(el.dataset.tex, el, { displayMode: true, throwOnError: false });
        el.dataset.rendered = "1";
      } catch (_) { el.textContent = el.dataset.tex; }
    });
    container.querySelectorAll(".chat-katex-inline").forEach(el => {
      if (el.dataset.rendered) return;
      try {
        katex.render(el.dataset.tex, el, { displayMode: false, throwOnError: false });
        el.dataset.rendered = "1";
      } catch (_) { el.textContent = el.dataset.tex; }
    });
  }

  // ── Build DOM ───────────────────────────────────────────

  // FAB button
  const fab = h("button", "chat-fab");
  fab.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>`;
  fab.title = "Chat with Folio";
  document.body.appendChild(fab);

  // Chat panel
  const panel = h("div", "chat-panel");
  panel.innerHTML = `
    <div class="chat-header">
      <div class="chat-header-left">
        <span class="chat-avatar">F</span>
        <span class="chat-title">Folio</span>
        <span class="chat-subtitle">editorial assistant</span>
      </div>
      <div class="chat-header-right">
        <button class="chat-clear-btn" title="Clear conversation">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
        </button>
        <button class="chat-close-btn" title="Close">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
    </div>
    <div class="chat-messages" id="chat-messages">
      <div class="chat-welcome">
        <div class="chat-welcome-icon">F</div>
        <div class="chat-welcome-text">
          <strong>Hi! I'm Folio</strong>, your editorial assistant.<br>
          Ask me about the paper's content, status, or anything else.
        </div>
        <div class="chat-welcome-suggestions" id="chat-welcome-suggestions"></div>
      </div>
    </div>
    <div class="chat-input-area">
      <div class="chat-suggestions" id="chat-suggestions"></div>
      <div class="chat-input-row">
        <textarea class="chat-input" id="chat-input" placeholder="Ask about the paper..." rows="1"></textarea>
        <button class="chat-send" id="chat-send" title="Send">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
        </button>
        <button class="chat-stop" id="chat-stop" title="Stop" style="display:none">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>
        </button>
      </div>
    </div>`;
  document.body.appendChild(panel);

  // Element refs
  const messagesEl = $("#chat-messages", panel);
  const inputEl = $("#chat-input", panel);
  const sendBtn = $("#chat-send", panel);
  const stopBtn = $("#chat-stop", panel);
  const clearBtn = $(".chat-clear-btn", panel);
  const closeBtn = $(".chat-close-btn", panel);
  const suggestionsEl = $("#chat-suggestions", panel);
  const welcomeSuggestions = $("#chat-welcome-suggestions", panel);

  // ── Welcome suggestions ─────────────────────────────────
  function renderWelcomeSuggestions() {
    const defaults = [
      "What is this paper about?",
      "Show paper status",
      "What needs work?",
    ];
    welcomeSuggestions.innerHTML = "";
    for (const s of defaults) {
      const chip = h("button", "chat-chip", esc(s));
      chip.onclick = () => sendMessage(s);
      welcomeSuggestions.appendChild(chip);
    }
  }
  renderWelcomeSuggestions();

  // ── Toggle panel ────────────────────────────────────────
  function toggleChat() {
    chatOpen = !chatOpen;
    panel.classList.toggle("open", chatOpen);
    fab.classList.toggle("hidden", chatOpen);
    if (chatOpen) {
      inputEl.focus();
      scrollToBottom();
    }
  }

  fab.onclick = toggleChat;
  closeBtn.onclick = toggleChat;

  // ── Clear conversation ──────────────────────────────────
  clearBtn.onclick = () => {
    if (isStreaming) return;
    messages = [];
    messagesEl.innerHTML = "";
    // Re-add welcome
    const welcome = h("div", "chat-welcome");
    welcome.innerHTML = `
      <div class="chat-welcome-icon">F</div>
      <div class="chat-welcome-text">
        <strong>Hi! I'm Folio</strong>, your editorial assistant.<br>
        Ask me about the paper's content, status, or anything else.
      </div>`;
    const ws = h("div", "chat-welcome-suggestions");
    welcome.appendChild(ws);
    messagesEl.appendChild(welcome);
    renderWelcomeSuggestions();
    suggestionsEl.innerHTML = "";
  };

  // ── Input handling ──────────────────────────────────────
  inputEl.addEventListener("input", () => {
    // Auto-resize textarea
    inputEl.style.height = "auto";
    inputEl.style.height = Math.min(inputEl.scrollHeight, 120) + "px";
  });

  inputEl.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  sendBtn.onclick = () => sendMessage();

  stopBtn.onclick = () => {
    if (abortController) {
      abortController.abort();
      abortController = null;
    }
  };

  // ── Render messages ─────────────────────────────────────
  function addUserMessage(text) {
    const el = h("div", "chat-msg chat-msg-user");
    el.innerHTML = `<div class="chat-bubble chat-bubble-user">${esc(text)}</div>`;
    messagesEl.appendChild(el);
    scrollToBottom();
  }

  function addAssistantMessage() {
    const el = h("div", "chat-msg chat-msg-assistant");
    const avatar = h("span", "chat-msg-avatar", "F");
    const bubble = h("div", "chat-bubble chat-bubble-assistant");
    const status = h("div", "chat-status");
    const content = h("div", "chat-content");

    bubble.appendChild(status);
    bubble.appendChild(content);
    el.appendChild(avatar);
    el.appendChild(bubble);
    messagesEl.appendChild(el);
    scrollToBottom();

    return { el, status, content, bubble };
  }

  function scrollToBottom() {
    requestAnimationFrame(() => {
      messagesEl.scrollTop = messagesEl.scrollHeight;
    });
  }

  // ── Suggestion chips ────────────────────────────────────
  function renderSuggestions(suggestions) {
    suggestionsEl.innerHTML = "";
    if (!suggestions || !suggestions.length) return;
    for (const s of suggestions) {
      const chip = h("button", "chat-chip", esc(s));
      chip.onclick = () => {
        suggestionsEl.innerHTML = "";
        sendMessage(s);
      };
      suggestionsEl.appendChild(chip);
    }
  }

  // ── Status indicator ────────────────────────────────────
  function renderStatus(statusEl, text) {
    if (!text) {
      statusEl.style.display = "none";
      statusEl.innerHTML = "";
      return;
    }
    statusEl.style.display = "";
    statusEl.innerHTML = `
      <div class="chat-status-inner">
        <span class="chat-status-dots">
          <span class="chat-dot"></span>
          <span class="chat-dot"></span>
          <span class="chat-dot"></span>
        </span>
        <span class="chat-status-text">${esc(text)}</span>
      </div>`;
  }

  // ── Send message ────────────────────────────────────────
  async function sendMessage(text) {
    text = text || inputEl.value.trim();
    if (!text || isStreaming) return;

    inputEl.value = "";
    inputEl.style.height = "auto";
    suggestionsEl.innerHTML = "";

    // Remove welcome if present
    const welcome = $(".chat-welcome", messagesEl);
    if (welcome) welcome.remove();

    // Add user message
    messages.push({ role: "user", content: text });
    addUserMessage(text);

    // Start streaming
    isStreaming = true;
    sendBtn.style.display = "none";
    stopBtn.style.display = "";
    inputEl.disabled = true;

    const assistant = addAssistantMessage();
    let fullText = "";

    abortController = new AbortController();

    try {
      const ctx = getPaperContext();
      const payload = {
        messages: messages.map(m => ({ role: m.role, content: m.content })),
        context: ctx,
        mode: "read",
      };

      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        signal: abortController.signal,
      });

      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() || "";

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;
          const data = line.slice(6).trim();

          if (data === "[DONE]") continue;
          if (!data) continue;

          try {
            const evt = JSON.parse(data);

            if (evt.error) {
              assistant.content.innerHTML = `<div class="chat-error">${esc(evt.error)}</div>`;
              renderStatus(assistant.status, "");
              break;
            }

            if (evt.status) {
              renderStatus(assistant.status, evt.status);
              scrollToBottom();
            }

            if (evt.text) {
              fullText += evt.text;
              renderStatus(assistant.status, "");
              // Incrementally render markdown
              assistant.content.innerHTML = chatMdToHtml(fullText);
              renderChatMath(assistant.content);
              scrollToBottom();
            }

            // Clear status event (empty object)
            if (!evt.text && !evt.status && !evt.error) {
              renderStatus(assistant.status, "");
            }
          } catch (e) {
            // Skip malformed JSON
          }
        }
      }
    } catch (e) {
      if (e.name === "AbortError") {
        if (!fullText) {
          assistant.content.innerHTML = '<div class="chat-stopped">Stopped</div>';
        }
      } else {
        assistant.content.innerHTML = `<div class="chat-error">${esc(e.message)}</div>`;
      }
      renderStatus(assistant.status, "");
    }

    // Finalize
    isStreaming = false;
    abortController = null;
    sendBtn.style.display = "";
    stopBtn.style.display = "none";
    inputEl.disabled = false;
    inputEl.focus();

    if (fullText) {
      messages.push({ role: "assistant", content: fullText });
      // Extract and render suggestions
      const suggestions = extractSuggestions(fullText);
      if (suggestions.length) {
        renderSuggestions(suggestions);
      }
      // Final render pass for math
      renderChatMath(assistant.content);
    }

    scrollToBottom();
  }

  // ── Keyboard shortcut (Cmd/Ctrl + K) ───────────────────
  document.addEventListener("keydown", (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === "k") {
      e.preventDefault();
      toggleChat();
    }
    if (e.key === "Escape" && chatOpen) {
      toggleChat();
    }
  });

})();
