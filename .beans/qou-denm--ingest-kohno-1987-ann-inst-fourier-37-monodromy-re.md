---
# qou-denm
title: Ingest Kohno 1987 (Ann. Inst. Fourier 37, monodromy representations of braid groups and Yang–Baxter) and Drinfeld 1985 (Soviet Math. Dokl.) into library/ — both cited by conj:hecke-monodromy-step-two and KZPullbackHypothesis.lean, neither held
status: todo
type: task
created_at: 2026-09-07T10:16:41Z
updated_at: 2026-09-07T10:16:41Z
---

Opened 2026-09-07 (KZ plan step 6, PR #7035 §B). references.ts has kohno1987 and drinfeld1985; library/ has no directory for either, so every 'Kohno–Drinfeld gives the Hecke quadratic' sentence in the corpus is unverifiable by corpus-grep path 5. Kohno 1987 is open access on NUMDAM (Annales de l'Institut Fourier); Drinfeld 1985 (Soviet Math. Doklady 32) is not open access — record as cited-only if it cannot be obtained legitimately. Use the document-intake skill (uploads/ → library/<doc-id>/ via folio-assistant's pdf-structure + extract-candidates), then summarize-library.py --apply. Low priority: nothing computational depends on it.
