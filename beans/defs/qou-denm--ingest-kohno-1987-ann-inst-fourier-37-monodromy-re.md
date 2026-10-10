---
# qou-denm
title: Ingest Kohno 1987 (Ann. Inst. Fourier 37, monodromy representations of braid groups and Yang–Baxter) and Drinfeld 1985 (Soviet Math. Dokl.) into library/ — both cited by conj:hecke-monodromy-step-two and KZPullbackHypothesis.lean, neither held
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T10:16:41Z
updated_at: 2026-10-04T15:20:53Z
parent: qou-mub3
---

Opened 2026-09-07 (KZ plan step 6, PR #7035 §B). references.ts has kohno1987 and drinfeld1985; library/ has no directory for either, so every 'Kohno–Drinfeld gives the Hecke quadratic' sentence in the corpus is unverifiable by corpus-grep path 5. Kohno 1987 is open access on NUMDAM (Annales de l'Institut Fourier); Drinfeld 1985 (Soviet Math. Doklady 32) is not open access — record as cited-only if it cannot be obtained legitimately. Use the document-intake skill (uploads/ → library/<doc-id>/ via folio-assistant's pdf-structure + extract-candidates), then summarize-library.py --apply. Low priority: nothing computational depends on it.

## 2026-09-13 — BLOCKED ON EGRESS, not on licensing; and the exposure is smaller than this bean assumed

**Both papers are unobtainable from this container, and the reason is not the one
the bean anticipated.** The bean expected Kohno to be fetchable (NUMDAM open
access) and only Drinfeld to be a licensing problem. Measured:

| host | probe | result |
|---|---|---|
| `www.numdam.org` | `curl http://www.numdam.org/item/AIF_1987__37_4_139_0.pdf` | **403** — `Host not in allowlist: www.numdam.org.` |
| `arxiv.org` | `curl http://arxiv.org/abs/math/0605041` | **403** — `Host not in allowlist: arxiv.org.` |
| `github.com` (git) | `curl .../info/refs?service=git-upload-pack` | 200 (control passes) |
| `pypi.org` | `curl https://pypi.org/simple/` | 200 (control passes) |

`selective` is reported `false` by `$HTTPS_PROXY/__agentproxy/status`, but the
gateway plainly answers with an allowlist denial naming the host, so an
allowlist is in force at the gateway. **The generalisation is the useful part:
`arxiv.org` is blocked too, so NO document intake of any kind is possible from
this environment — `qou-denm` is not a special case, and neither is NUMDAM.**
The `sandbox-egress` route table (route 1 github, route 2 pip-bundled fixtures,
route 3 env override) has no route for a journal PDF: it is not on a git repo,
not in a wheel, and the tool has no data-URL override.

**Exposure, measured — 0 sorries, 1 prose sentence.** The bean says "every
'Kohno–Drinfeld gives the Hecke quadratic' sentence in the corpus is
unverifiable". Counted:

* **8 `.lean` files** carry a `-- Ref:` to `[kohno1987]` or `[drinfeld1985]`
  (`KZFlatnessLevelIndependent`, `HeckeQuadraticClassicalShadow`,
  `KZLevelFromHeckeNormalisation`, `HeckeMonodromy`, `KZUnitModulusPrune`,
  `KZPullbackHypothesis`, `mass-theory/lifted-crossing-locality`,
  `braids-and-knots/r-matrix-braiding-structure`). **Every one has `sorry = 0`
  and `axiom = 0`.** So no unproved Lean statement is being discharged by an
  unreadable citation — these are docstring context, not AGENTS.md §1
  `sorry`-justifications. That is the sharp question and the answer is clean.
* **3 content blocks** carry the keys in `cites[]`, but only **one**
  (`conj:hecke-monodromy-step-two`) states a claim from them in prose:
  *"The literature model is Kohno--Drinfeld: the monodromy of a
  Knizhnik--Zamolodchikov connection factors through $H_n(q)$."* — correctly
  hedged as the literature model, and everything the block derives from it
  (`KZFlatnessLevelIndependent`, `SL2QuantumTraceIsZD`, the level arithmetic)
  is separately Lean-proved. `lifted-crossing-locality` and
  `q-holonomy-locality-derivation` cite `kohno1987` in the `.ts` manifest and
  **never mention Kohno in the `.md` at all** — a manifest-only citation with
  no textual claim behind it. Whether that is a defect is a judgement call and
  is NOT being acted on here (§"ASK THE OWNER BEFORE CHANGING THINGS").

**Two things the paper would settle that nothing here can.** (1) The
`drinfeld1985` entry's own note is a self-declared `PLACEHOLDER` asking
*"verify whether the QOU Lean Ref intends the 1985 Doklady note or the 1986 ICM
address"* — unresolvable without a copy. (2) The `kohno1987` note asserts the
paper "Proves that monodromy of the KZ connection on $X_n$ coincides with the
quantum-group R-matrix representation of $U_q(g)$"; that is the standard
statement of the Kohno half of Kohno–Drinfeld and is very likely right, but it
is **recalled, not read**, and this bean exists precisely to stop that class of
sentence.

**Status stays `todo`.** What a network-open environment should run: add
`www.numdam.org` to the environment's egress allowlist, fetch
`http://www.numdam.org/item/AIF_1987__37_4_139_0.pdf` (DOI 10.5802/aif.1075),
then `document-intake` (`uploads/` → `library/<doc-id>/`) +
`summarize-library.py --apply`, and add a `library:` block to the `kohno1987`
entry in `references.ts` in the shape `faddeev1995` uses. Drinfeld 1985 (Soviet
Math. Dokl. 32, 254–258) has no open-access copy and should be recorded
cited-only regardless of egress.
