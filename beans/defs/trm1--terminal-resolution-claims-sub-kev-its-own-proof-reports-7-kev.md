---
# trm1
title: prop:terminal-resolution claims sub-keV; its own proof reports ~7 keV
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T12:40:00Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-q4oa
---

Surfaced by the adversarial second reader on PR #4921 (bean `fwr11`) while
refuting a proposed `uses[]` edge, and verified independently before filing.
Not fixed here: this is a content claim, not bookkeeping.

[`prop:terminal-resolution`](../folio/quantum-observable-universe/mass-theory/terminal-resolution.md)
opens *"the predictions match CODATA to **sub-keV** precision"* over a four-row
table:

| structure | formula asserted | QOU | CODATA |
|---|---|---|---|
| proton | $Q(q)\,\mathfrak{m}(\mathcal{L}_{\mathrm{Hopf}})_{uud}$ | 938.272 | 938.272 |
| neutron | $Q(q)\,\mathfrak{m}(\mathcal{L}_{\mathrm{Hopf}})_{udd}$ | 939.565 | 939.565 |
| deuteron | $\mathfrak{m}(L_6) - \text{Binding}$ | 1875.613 | 1875.613 |
| binding energy | $\Delta$ Skein polynomial | 2.224 | **2.225** |

Three problems, in increasing order of seriousness.

1. **The table contradicts its own caption.** The binding-energy row is
   2.224 vs 2.225 — a **1 keV** discrepancy on a table captioned "sub-keV".

2. **The proof reports a residual ~7x larger than the caption allows.**
   [`prf:terminal-resolution`](../folio/quantum-observable-universe/observations/terminal-resolution-proof.md)
   closes: *"These reproduce the CODATA proton and neutron masses to within a
   $-0.53\%$ residual on the splitting $m_n - m_p$."* At
   $m_n - m_p = 1.2933$ MeV that is **6.9 keV**.

3. **The proof does not establish the table.** It derives only $m_p$ and $m_n$,
   and by a different route than the table states — dressed quark masses summed
   over Skein pairs, $m_p = \mathcal{S}_{uu} + 2\mathcal{S}_{ud}$, with
   $\mu_u \approx 311.10$, $\mu_d \approx 312.39$ MeV — never using $Q(q)$ or
   $\mathfrak{m}(\mathcal{L}_{\mathrm{Hopf}})$. The deuteron row and the
   binding-energy row are never derived at all.

So either the proof belongs to a different statement, or the proposition
asserts more than anything proves. The parent declares
`proofs: ["prf:terminal-resolution"]`, so the corpus says they are a pair.

They also sit in different chapters — parent in `mass-theory` (Ch 12), proof in
`observations` (Ch 14).

## Suggested disposition (author's call)

- Scope the caption to what is shown: p and n, to the stated 0.53 % on the
  splitting. "Sub-keV" is not supported by either the proof or the table's own
  binding row.
- Either derive the deuteron / binding rows or move them to a block that does.
- Reconcile the two routes, or say plainly that the table's formula column is
  aspirational and the proof's route is the one that runs.

## Partly done — PR #5008 (2026-08-11)

The "worth checking first" line below was right: the caption was the outlier,
not the number. `rem:dressed-quark-numerology-at-q0` already stated the
$-0.53\%$ residual plainly, so the *caption* half of problems 1 and 2 was a
wording fix and is landed: it now scopes to the splitting, quotes 6.9 keV, and
says which rows are not derived here. The 1 keV binding-row discrepancy itself
is untouched — the row still reads 2.224 against CODATA 2.225; what changed is
that the caption no longer contradicts it.

Still open, both derivation work and both author's call:

- **The two routes are unreconciled.** Formula column: $Q(q)$ on a Hopf-link
  mass. Proof: Skein crossing pairs over dressed quark masses. Sharper than the
  original filing put it — the p/n rows cannot simultaneously agree to three
  decimals *and* carry a 6.9 keV residual on their difference, so the table and
  the proof are not reporting the same computation, and at most one of them is
  the block's actual content.
- **The deuteron and binding rows are still underived here.** Not checked
  whether `mba-step09b-per-isotope-binding` derives them; the caption therefore
  claims only what was verified.

Related: the `-0.53\%` is attributed in-text to *"the dropped
$O((\Delta m/M_N)^2)$ correction to `prop:flavor-split-substrate`"* — so the
size of the residual may already be understood, and only the caption is wrong.
That would make this a one-line fix rather than a derivation gap. Worth
checking first.

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

Caption fixed (PR #5008). Still open: p/n rows reproduce an input (μ̄ ≈ M_N/3 in dressed-quark-numerology-at-q0), only m_n − m_p is predicted; formula column vs proof route unreconciled; deuteron/binding rows underived. Options on the owner card.

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.

Ruling check: the finding (p/n rows reproduce the M_N input) is about the table's honesty, not about which trace or knot is used; the formula column's Hopf-link wording predates the electron ruling and is a separate label question, not relied on here.
