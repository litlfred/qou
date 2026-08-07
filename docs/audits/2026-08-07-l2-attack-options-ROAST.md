# ROAST — adversarial pass on my own L2 attack options

**Date:** 2026-08-07 · **Branch:** `claude/1ppq-l2-closure-attacks-ufrfun` · **PR #4664**
**Companion to:** [`2026-08-07-l2-closure-attack-options-non-em-terms.md`](2026-08-07-l2-closure-attack-options-non-em-terms.md)
**Beans:** session `qou-kemt`, children `qou-78pt qou-fvzm qou-l2t2 qou-ubsl qou-nvoq qou-se8k qou-4q9h qou-3wxk qou-pnhy qou-orvl qou-40r8 qou-imcd`

Owner asked for a roast. Run under the Critical-distance license. **Two findings
below are outright errors in the companion memo**, not quibbles; both are corrected
in the memo itself in the same commit.

---

## R0. The two memo errors, up front

### R0.1 — The 0.12 % coincidence was convention-shopped (most serious)

The memo's §4.3 reports `ln[3]_q/ln[2]_q = 1.5871` vs `r* = 1.5852` (0.12 %) using
**symmetric** q-integers `[2]_q = q^{1/2}+q^{−1/2}`, `[3]_q = q+1+q^{−1}`.

That convention was **my convenience, not a derivation.** The scratch check also
computed the unsymmetrized convention `[n]_q = (qⁿ−1)/(q−1)`:

| convention | `ln[3]_q/ln[2]_q` | vs `r* = 1.5852` |
|---|---:|---:|
| symmetric (reported in memo) | 1.58708 | **0.12 %** |
| unsymmetrized (computed, **not reported**) | 1.61593 | **2.0 %** |

I ran both and put the flattering one in the memo. That is exactly the
shape-probing the repo bans, committed by the agent writing the anti-shape-probing
section. The honest statement is: **the agreement is a function of an arbitrary
convention choice, and therefore currently means nothing.**

This does not kill the underlying structural idea (§3 of the memo — that the Markov
normalization carries the extensive piece). It kills the *numerical* claim
attached to it. The probe `qou-l2t2` must **derive** the normalization factor from
the Markov moves *first* and evaluate whatever comes out — never select the
convention afterwards. Memo §4.3 now carries both rows.

### R0.2 — "A3 closes Class III" is a scale conflation (fatal to that claim)

The memo says the SU(4)-Casimir option closes the `(N−Z)²/A` term *"and Class III
(`m_n`, `Δ_pn`, `Q_β`)"* because the gating witness says "no flavor-split."

Run the numbers:

| quantity | value |
|---|---:|
| `Δ_pn` current absolute error | 0.977 eV |
| **`Δ_pn` L2 100× target** | **0.0061 eV** |
| `m_n` current absolute error | 2.24 eV |
| nuclear binding per nucleon | ~8 MeV = 8×10⁶ eV |
| **orders of magnitude between the L2 target and the nuclear scale** | **≈ 9.1** |

Closing `Δ_pn` at L2 requires the categorical p/n mass split — a 1.29 MeV quantity —
to **6 meV**. Nuclear symmetry energy is a ~20 MeV/nucleon effect. These two
problems share the word "isospin" and nothing else. **A binding fix accurate to 1 %
is still 10⁹ times too coarse to touch Class III.**

So the memo's prioritisation is wrong where it links binding attacks to the L2
dashboard. Corrected position: **binding is a Subgoal-1 story only.** The L2
dashboard misses (all three classes) are ppb-scale problems in the *absolute mass /
weak-sector* chain and are not addressed by any option A1–A7. Bean `qou-40r8`
carries this and now blocks `qou-ubsl`.

This matters for what the owner actually asked. "Attack options to close 1 ppQ L2"
and "get binding correct" turn out to be **two different programs**. The memo
answered the second while claiming credit against the first.

---

## R1. Per-option roast

### A1 — unnormalized trace (memo §3) · `qou-78pt`
**Severe.** "Just don't normalize" is not a well-defined instruction — it is a
**one-parameter family**. Kauffman bracket, Ocneanu/Markov trace, and the HOMFLY
specialization differ by factors of `(−q^{1/2}−q^{−1/2})` and by writhe-dependent
`a^{−w}` terms. Each gives a different extensive coefficient. Choosing the member
that lands on `a_V ≈ 15.6` **is a fit**, and it is a fit with a free continuous
parameter dressed as a structural insight.

Second, **strands-per-nucleon is undetermined.** If a nucleon is one strand the
extensive coefficient is `E₀·log N`; if it is a 3-component Borromean link it is
`3·E₀·log N`. Nobody has fixed this. That is another undeclared factor of 3.

Numerically the `N=2` reading gives ~2.91 MeV/strand against `a_V ≈ 15.6` — **5.4×
short**, or 1.8× short at 3 strands/nucleon. Needing "a factor" is precisely the
condition under which a convention family becomes a fit.

**Verdict:** the structural observation (isotopy-invariance ⇒ intensive ⇒ the
extensive piece is what normalization removes) is sound and worth keeping. The
option is **unfalsifiable as written** until the normalization is pinned from the
axioms. That pinning is the actual work; everything else is downstream.

### A2 — Ocneanu `N` consistency · `qou-fvzm`
**Near-fatal, and I undersold it.** The T3f audit's own §3a says: if `N=2` is derived
(forced by Descartes), the eightfold way **cannot** use `N=3` from the same Hecke
machinery — *"this is the position the current chapter takes."* My option proposes
the branch the chapter has already argued against.

Worse, and I noted it only in passing: the audit states plainly that **changing `N`
changes all mass predictions.** The framework's *successes* — `m_μ/m_e`, `m_p`,
`m_K/m_π` (one of only two L2 passes) — live at `N=2`. An `N=3` binding fix that
breaks the proton mass is not a fix. This is a **regression risk**, and the memo
framed it as upside.

**Verdict:** demote. Any `N=3` probe must *first* show it does not destroy the
existing predictions. That precondition is most of the cost and it is likely to fail.

### A3 — SU(4) Casimir · `qou-ubsl`
Three objections, one structural.

1. **The Casimir gives `(N−Z)²`, not `(N−Z)²/A`.** The `1/A` comes from Fermi-gas
   level density — a *separate dynamical input*. The memo claimed the Casimir
   supplies the shape. It supplies the numerator. Corrected in the memo.
2. **Descartes may forbid the SU(4) reading outright.** The Descartes condition
   forces `dim V = 2`. Schur–Weyl on `V^{⊗n}` with `dim V = 2` gives the `GL(2)`
   commutant — **not `GL(4)`**. Wigner's SU(4) is spin⊗isospin, `dim = 4`. Whether
   the framework's `λ ⊢ n` can carry spin-isospin content at all is an open
   structural question, not a lookup. Resolve before any work.
3. Wigner SU(4) is badly broken by spin-orbit above `A ≈ 40`; anything built on it
   inherits that.

**Verdict:** objection 2 is a potential hard stop. Cheap to check, must go first.

### A4 — pairing = Δ_λ sign · `qou-nvoq`
**Possibly dead on arrival, and cheaply so.** The BW pairing term is three-valued —
even-even `+`, odd-odd `−`, odd-`A` `0` — which needs the parities of `N` and `Z`
**independently**: two bits. `(−1)^{n(λ)}` is **one bit**. A single ℤ/2 cannot carry
two independent parities.

It is not quite dead: `A = N+Z` parity is separately available, and (one bit from
`n(λ)`) + (one bit from `A`) could in principle span the three cases. But that is a
different, weaker claim than the memo's "you may already own this term."

**Verdict:** still the cheapest probe and still worth running, but expectation
should be *"probably refutes"*, not *"may already own a BW term."* A clean negative
is the likely and still-useful outcome.

### A5 — IMME · `qou-se8k`
**Weaker than advertised.** IMME constrains the **charge-dependent** (isospin-
breaking) sector. The missing extensive term is **isoscalar by hypothesis** — so
IMME's small `d` coefficient says nothing whatsoever about it. My memo's claim that
IMME "kills every 3-body candidate built on p/n asymmetry" is true but **those were
already excluded** by the option-e ledger (the color-tube weight fixes sign, not
magnitude). Marginal value is therefore low.

Also the rank-≤2 result assumes first-order perturbation theory; isospin mixing and
second-order effects generate `d` terms independently, so "small `d` ⇒ no 3-body" is
not airtight even within its own domain.

**Verdict:** demote from #2 to optional. It re-derives a known negative by a new
route. That has some confirmatory value and near-zero closure value.

### A6 — hypernuclei · `qou-4q9h`
The ⅔ well-depth ratio is a **quark-counting** result. QOU does not have quarks as
fundamental objects — it has strands and braid closures. "Replace one of three
light quarks" ↦ "change one strand's flavor" is an **assumption about the
quark–strand dictionary**, not a derivation from it. If that dictionary is wrong,
the prediction is meaningless rather than falsified.

Also, and this is a framing error in the memo: hypernuclei **validate or refute**.
They do not close a gap. The memo listed it among "attack options" as if it could
supply the missing term. It cannot.

**Verdict:** genuinely novel and genuinely valuable — as an *independent test*,
correctly labelled. Not a closure route.

### A7 — chiral EFT / Tjon · `qou-3wxk`
Importing chiral EFT imports a **different EFT's power counting** (`Q/Λ_χ`). QOU has
its own expansion parameter (`u = b·ℏ_q² ≈ 0.00852`). There is no argument that the
two hierarchies align, and using chiral-EFT magnitudes as a "budget" smuggles in
precisely the nuclear phenomenology the framework exists to replace.

**Verdict:** usable only as a *placement* diagnostic (where does QOU sit relative to
the Tjon locus), never as a magnitude input. Narrow but legitimate in that form.

---

## R2. The meta-roast — what all six options share

**Every option assumes the missing piece is a term.** Six ansätze have already
failed. A seventh through twelfth failing the same way would be evidence for a
different diagnosis: that the **atomic-braid → nucleus map itself** is the defective
step, not the trace or its normalization. If the geometry (which strands are which
nucleons, how many strands per nucleon, what the closure is) is wrong, then *every*
add-a-term attack fails identically — which is exactly the observed pattern.

Nobody has tested the map. Bean `qou-imcd`. The cheap first probe is
**A-scaling-exponent-only**: does the framework reproduce the *exponent* of any
A-dependent observable, with magnitude entirely free? If it cannot get the exponents
right with magnitude free, the missing object is not a magnitude and no term will
save it.

**Second meta-point.** The memo's own §2.1 argues that exponents are structure and
coefficients are numerology — then §4.3 proceeded to shop a coefficient across
conventions. The discipline was stated and immediately violated in the same
document. Worth noting as a failure mode: *stating* an anti-fit rule provides no
protection against violating it two sections later.

---

## R3. Revised recommendation

The memo's ordering was built on the (wrong) premise that binding attacks serve the
L2 dashboard. With R0.2 corrected:

| # | Item | Why first |
|---|---|---|
| 1 | **`qou-40r8`** — settle whether binding touches L2 at all | Decides if this whole arc is Subgoal-1-only. Costs an hour. Everything else is contingent on it. |
| 2 | **`qou-ubsl` objection 2** — does Descartes `dim V = 2` forbid the SU(4) reading? | Potential hard stop, cheap lookup |
| 3 | **`qou-imcd`** — exponent-only test of the braid→nucleus map | If this fails, options A1–A7 are all moot |
| 4 | **`qou-nvoq`** — Δ_λ-sign parity check | Cheapest; expect a negative |
| 5 | **`qou-78pt`** — pin the Markov normalization *from the axioms* | The real work behind A1; unfalsifiable until done |
| 6 | `qou-orvl`, `qou-pnhy` — ledger/doc re-scopes | Housekeeping, independent of results |

`qou-fvzm` (Ocneanu `N=3`) and `qou-se8k` (IMME) drop below the line pending 1–3.
`qou-4q9h` (hypernuclei) stays valuable but is relabelled *validation*.

**Net after the roast:** of eight proposed attacks, one is unfalsifiable as written
(A1), one is near-fatally blocked by the framework's own position and its successes
(A2), one may be structurally forbidden (A3), one is likely to refute cheaply (A4),
one re-derives a known negative (A5), one is validation not closure (A6), one is
narrow (A7) — and the most valuable item is the one the memo did not propose at all:
**test the geometry, not the terms** (R2).
