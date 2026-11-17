---
# qou-98g5
title: 'DEFECT: corpus conflates 1/delta = 0.497290545 with convention-C z = 0.499320334 -- different elements, 0.408% apart'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T17:08:37Z
updated_at: 2026-11-17T07:34:00Z
parent: qou-cdx1
---


Branch: claude/anchor-followups-2026-08-08. Found by workflow wz3teraa6
(4 agents, 503k tokens) while checking whether the Temperley-Lieb Gram
determinant closes T4 by citation. It does not -- but it found this.

## THE TWO NUMBERS

  1/delta   = 1/[2]_q = 1/(q + 1/q)          = 0.497290545604915555995839
  z_C       = 1/(q^1/2 + q^-1/2)             = 0.499320334183694452413443

They differ by 0.408 %. They are `1/(x + 1/x)` at x = q and at x = sqrt(q) --
ONE SQUARE ROOT APART. That is why they are so easy to conflate, and it is also
the diagnosis: the framework's balanced q IS Jones's t^(1/2), so convention C is
1/delta read one square root too early.

THEY ARE NOT THE SAME OBJECT. delta is the TL loop parameter, attached to the
TL generator e_i. z is the Ocneanu/Markov parameter, attached to the HECKE
generator sigma_i. Different elements of different algebras.

## THE CORRECT IDENTITY, verified to 60 dps with residual EXACTLY 0.0

  e_i := q - sigma_i     =>  e_i^2 = [2]_q e_i
  tr_M(x . e_n) = (q - z) tr_M(x)
  q - z_D = q - q^3/(q^2+1) = q/(q^2+1) = 1/[2]_q     identically in q

So delta = [2]_q = q + q^-1 = 2.010896866707122299752492, and CONVENTION D IS
THE STANDARD NORMALISED TEMPERLEY-LIEB MARKOV TRACE at that delta. Also
mu_- = (q-z)/(q+q^-1) = 1/delta^2 -- which is the 1/[2]_q^2 already proved as
y_mixed_conventionD. Now Lean-proved as
TemperleyLiebTower.loop_reciprocal : (q - z)(q + q^-1) = 1.

Corroborating, from four independent directions: Hecke eigenvalues {q, -1/q}
force E_i = q - sigma_i with E_i^2 = [2]_q E_i; the closed form
y_(n-k,k) = [n-2k+1]_q/[2]_q^n is verbatim the TL weight U_j(delta)/delta^n;
tl_cable.rs:13 sets A = q^(-1/2) and delta = -A^2 - A^-2; and q - z_D = 1/delta.

## CONFIRMED DEFECT SITES -- each says 1/delta and supplies the sqrt(q) number

  1. folio/quantum-observable-universe/mass-theory/
     h3-markov-wenzl-weights-context.md:69
       "The stipulated value 1/(q^{1/2}+q^{-1/2}) is the Temperley-Lieb loop
        reciprocal 1/delta -- correct for the TL generator e_i"
     FLATLY FALSE. 1/delta = 0.497291, not 0.499320. And this block's whole job
     is convention adjudication, which makes it the worst possible host.
  2. docs/coordination/convention-slip-registry.json:79
       "Value = delta^-1 (Temperley-Lieb loop reciprocal) where the TL trace
        parameter is delta^-2"
     THE CORPUS'S OWN DEFECT LEDGER CARRIES THE DEFECT.
  3. folio/quantum-observable-universe/mass-theory/
     reeb-linking-cwf-normalization.md:20
       "the exchange channel with the Markov conditional-expectation weight
        z = delta^{-1}"

Re-verify each line before editing -- the workflow's verifiers overturned about
one in five classifier findings elsewhere in this sweep, mostly on line numbers
and blast radius rather than on the substance.

## WHY IT MATTERS BEYOND TIDINESS

Site 1 is the block a reader consults to decide WHICH CONVENTION IS IN FORCE. It
currently tells them that the excised convention C is the TL loop reciprocal.
That is not a stale number; it is a wrong identification between two algebras,
and it will keep regenerating convention drift for as long as it stands. It also
means the C-vs-D excision cannot be called complete while the registry's own
sibling ledger asserts the conflation.

## FIX

  [ ] Rewrite site 1 to state: delta = [2]_q = q + q^-1; 1/delta = q - z under
      convention D; 1/(q^1/2+q^-1/2) is NEITHER, and is the excised convention-C
      Ocneanu parameter on the HECKE generator. Cite
      TemperleyLiebTower.loop_reciprocal.
  [ ] Fix site 2 in convention-slip-registry.json, and check whether the
      registry's schema/validator can be taught to catch this class -- it is a
      wrong SYMBOL-to-VALUE binding, which is exactly what the proposed
      `trace-convention` QA axis (detangler decision 8) should detect.
  [ ] Fix site 3.
  [ ] Sweep for further sites: grep for "loop reciprocal", "delta^-1",
      "delta^{-1}", "1/delta", "Temperley" near any 0.4993 or q^{1/2} form.
      The three above came from one workflow angle, not an exhaustive pass.

---

## Update 2026-08-09 — `1/δ` now has a *derived* identity, not just a value

`QOU/QBeta/JonesNormalisation.lean` (commit `cfe4921eb`) turns the distinction
this bean records from a numeric coincidence into a theorem, which makes future
conflations refutable rather than merely suspicious.

Put `eᵢ := q − σᵢ`. From the Hecke quadratic relation alone (`tl_generator_sq`,
no trace and no convention needed):

    eᵢ² = [2]_q · eᵢ

so `δ = [2]_q = q + q⁻¹` is **the Temperley–Lieb loop parameter**, full stop. And
convention D is exactly the statement

    tr_M(eᵢ) = q − z = 1/δ        i.e.  (q − z)·[2]_q = 1

(`TemperleyLiebTower.loop_reciprocal`). So:

* **`1/δ = 0.497290545604915556` is `tr_M(eᵢ)`** — the trace of the TL
  *projector-scaled* generator. It is the loop reciprocal.
* **`z = tr_M(σᵢ)`** — the trace of the *braid* generator. Under production D
  that is `0.612688037146465252`, not `0.499320334183694452`.
* **`z_C = 0.499320334183694452` is neither.** It is `1/[2]_{√q}`, the loop
  reciprocal at *half* argument, and `q^{1/2}+q^{-1/2}` is not a Markov parameter
  of the Hecke generator at all.

The 0.408 % gap this bean measured is therefore the gap between `[2]_q` and
`[2]_{√q}` — two different loop parameters — and the reason a C-era formula can
look almost right is that those two numbers are close, not that the objects are
related.

### One site fixed by it

`markov-pair-z2`'s Hopf-link normalisation
`J_Hopf = -(q^{1/2}+q^{-1/2})·z²` was exactly this conflation, and is now
retracted and replaced with the derived formula
`V = q^{-2e}·[2]_q^{n-1}·tr_M(β)`, `t = q^{-2}` — no square roots anywhere,
checked on four closures (`cfe4921eb`).

### Still open on this bean

The other conflation sites. **Grep for the half-argument form used as a loop
value**, not for the numbers — the symbolic form is the larger surface, as the
`c-formula-unlabelled` detector showed (`e6c7d599b`). A site is wrong when
`q^{1/2}+q^{-1/2}` appears as *the loop parameter of `tr_M`* or as *the Markov
parameter*; it is fine in a Wenzl positivity condition or a genuinely
half-argument skein, where it is `[2]_{√q}` on purpose.

## Round 63 Update (PR #8257)
- Formalized in PR https://github.com/litlfred/qou/pull/8257 (head `18cf0bc120a9baf3be0677bec0817855b4de7a7a`, Commit 1 `2b12359f227b0dc628cdd0df3e8f7f2f6ff6c5ca`, `scriptHash: 1bf530249a70`).
