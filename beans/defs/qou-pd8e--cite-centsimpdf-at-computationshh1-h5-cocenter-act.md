---
# qou-pd8e
title: Cite centsim.pdf at computations/hh1_h5_cocenter_action.py
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:35Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

Once the key exists, the probe's dim Z = 7 consistency check and its specialization-to-zeta_5 step should cite Sec. 5.1 and Thm 5.2 rather than asserting them.

**From the source**
- Sec. 5.1 (the class-polynomial centre basis) — For the generic Iwahori-Hecke algebra H of a finite Weyl group W, the elements z_C = sum_w ind(T_w)^{-1} f_C(T_w) T_{w^{-1}}, one per conjugacy class C of W, form an A-basis of the centre of H.
  Use here: The source of the 'Geck-Rouquier centre basis' the H_5(zeta_5) cocenter probe uses as its dim Z = 7 consistency check, currently asserted by name with no citation.
- Thm. 5.2 — For Iwahori-Hecke algebras the reduction map Z(H) -> Z(kH) on centres is surjective (the centre is stable under specialization).
  Use here: The statement that licenses computing the centre of H_5 after specializing to the Bring root of unity, which is the setting of the HH^0 / HH^1 computation; it is currently taken for granted.
- Thm. 3.3 / Thm. 5.4 — Under stated height-1 / height-2 prime conditions the number of simple modules of the specialized algebra equals that of a cyclotomic specialization -- the 'genericity' of the number of simple modules for Iwahori-Hecke algebras.
  Use here: The general control on how the Wedderburn block count behaves at a root of unity, which the corpus's root-of-unity Hecke work (H_5 at zeta_5) needs and currently reasons about case by case.

Source: `library/centsim/centsim.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/centsim/  ->  [geck-rouquier-centsim]
  Centers and Simple Modules for Iwahori-Hecke Algebras

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [geck-rouquier-centsim] as the citation key when you do it.

## 2026-11-21 — expo-cite-xcheck drain

Misaddressed: hh1_h5_cocenter_action.py makes no Geck–Rouquier or 'dim Z = 7' claim; it computes dim HH_0 directly over Z[ζ]. Nothing to cite there. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
