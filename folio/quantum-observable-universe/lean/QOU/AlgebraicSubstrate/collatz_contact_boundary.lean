import QOU.AlgebraicSubstrate.qou_obstruction_reduction

/-!
# QOU.AlgebraicSubstrate.collatz_contact_boundary

**Canonical declaration** for content block at
[`quantum-observable-universe/appendix-surreals/collatz-contact-boundary.ts`](quantum-observable-universe/appendix-surreals/collatz-contact-boundary.ts).

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

**C10 (2026-07-31).** The Kummer-removability content is no longer a standalone
context-class axiom. `CollatzContactBoundaryContext` now **extends** the universal
`QouObstructionReductionContext`, `kummer_obstruction_removable` is *defined* as
the vanishing of the level-2 Kummer obstruction, and
`obstruction_removable_of_even_chi` is **derived** (theorem, not field) from
`kappa_vanishes_iff_chi`. So "`2 ∣ χ(A)` ⟹ the `[2]_q`-divisor is removable" now
reduces to the universal χ(A) obstruction-reduction, not an independent assumption.
-/

namespace QOU.AlgebraicSubstrate


/-- QOU-furnished context for the `collatz_contact_boundary` claim. **Extends** the
    universal Kummer obstruction-reduction context (`QouObstructionReductionContext`,
    supplying `χ(A)`, `κ₀`, the level-`n` vanishing predicate and its definitional
    reduction), together with the Skein/Reeb data of a quantum observable universe
    `(𝐂, A, τ)` — `q` its substrate parameter, `[2]_q = q + 1` — and the Descartes
    specialisation `χ(A) = -6`. Kummer removability is no longer a field: it is
    *defined* below as level-2 obstruction vanishing and *derived* from parity. -/
class CollatzContactBoundaryContext (R : Type*) [CommRing R]
    extends QouObstructionReductionContext where
  /-- Substrate parameter `q` of the QOU, over the coefficient ring `R`.

      **Base ring (§7c).** This was `ℝ`, and that was a gratuitous
      specialisation: the manuscript's ambient object is the Skein module
      `𝒮(q) ≅ ℤ[q^{±1}]` — a Laurent ring — and the only thing done with `q`
      here is the ring identity `[2]_q = q + 1` and the hypothesis
      `[2]_q = 0` (i.e. `q = -1`, the residue-ring specialisation the prose
      describes). No ordering, no radical, no `Real.*` construct appears, so
      per AGENTS.md §7c this belongs over a generic commutative ring. -/
  q : R
  /-- The q-integer `[2]_q = q + 1`. -/
  q_int_2 : R
  q_int_2_eq : q_int_2 = q + 1
  /-- Descartes specialisation: `χ(A) = -6` (Bring's surface). -/
  chi_A_eq : chi_A = -6

/-- **Kummer-level-2 obstruction removable** := the level-2 Kummer obstruction
    *vanishes*. This is the manuscript's own identity — *"the obstruction vanishes;
    this means the `[2]_q`-divisor is removable"* — i.e. in Kummer theory the
    obstruction class **is** the removability criterion. -/
def kummer_obstruction_removable (R : Type*) [CommRing R]
    [CollatzContactBoundaryContext R] : Prop :=
  QouObstructionReductionContext.kappa_vanishes 2

/-- **`2 ∣ χ(A)` ⟹ the `[2]_q`-divisor is Kummer-removable — DERIVED** (formerly a
    raw context-class axiom `obstruction_removable_of_even_chi`). Removability is
    the vanishing of the level-2 obstruction (`kummer_obstruction_removable`), and
    `kappa_vanishes_iff_chi` reduces that vanishing to `2 ∣ χ(A)`. So the parity
    condition now discharges removability through the universal obstruction, with
    no independent assumption. -/
theorem obstruction_removable_of_even_chi {R : Type*} [CommRing R]
    [ctx : CollatzContactBoundaryContext R] (h : (2 : ℤ) ∣ ctx.chi_A) :
    kummer_obstruction_removable R := by
  unfold kummer_obstruction_removable
  exact (kappa_vanishes_iff_chi 2).mpr (by simpa using h)

/-- **Manuscript statement** (full body):

**Proposition (within a QOU with `2 ∣ χ(A)`; conditional on
[`conj:q-collatz`](#conj:q-collatz); "$[2]_q$-contact boundary").**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ whose Frobenius–Hopf object satisfies
$2 \mid \chi(A)$ — e.g. the Descartes universe, $\chi(A) = -6$; this
parity is what makes the $[2]_q$-divisor Kummer-removable, and
$\chi(A) = -6$ is a Descartes-universe property, not a general-QOU one —
and let $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2, \xi_q)$
be its Reeb bundle
([Reeb bundle](#def:reeb-bundle)) with $U(1)$ fiber
parametrized by $q = e^{i\varTheta}$, $\varTheta \in [0, 2\pi)$.

### From integer parity to the $[2]_q$-divisor

Classical Collatz hinges on a single question: is $n$ even
or odd?  Parity is residue mod $2$.  The number $2$ is
special: it is the smallest prime, the only even prime,
and the denominator of the halving step $n/2$.

In the QOU, the integer $2$ lifts to the quantum integer
$[2]_q = q + 1$ (combinatorial convention;
see [q-Collatz conjecture](#conj:q-collatz)).
The $[2]_q$-divisor is the locus where $[2]_q = 0$,
i.e. $q = -1$:

$$
  D_{[2]}  :=  \{q : [2]_q = 0\}
  =  \{-1\}.
$$

This is where the $q$-analog of "dividing by $2$"
degenerates — where the halving step ceases to exist.

**Kummer obstruction at the divisor.**
The point $q = -1$ belongs to $\mu_2$ (the 2nd roots
of unity).  The Kummer obstruction
([root-of-unity truncation](#prop:root-of-unity-truncation))
at level $n = 2$ asks: does $2$ divide $\chi(A) = -6$?
Yes — $6/2 = 3$.  The obstruction **vanishes**.  This
means the $[2]_q$-divisor is removable: the QOU axioms
can resolve the singularity.  At $q = -1$, the residue ring
is $\mathbb{Z}[q^{\pm 1}]/(q+1) \cong \mathbb{Z}$
(setting $q = -1$), and the $[2]_q$-adic valuation
specializes to the ordinary $2$-adic valuation.

### The $[2]_q$-adic valuation as contact order

For an element $P \in \mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$
of the Skein module, define the **$[2]_q$-adic valuation**:

$$
  v_{[2]}(P)  :=  \max\bigl\{k \geq 0 :
  [2]_q^k \mid P \text{ in } \mathbb{Z}[q^{\pm 1}]\bigr\}.


[…truncated; see manuscript for remainder…]

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). As of C10 the Kummer-removability half is no longer a raw axiom — it is derived from the universal obstruction-reduction (`obstruction_removable_of_even_chi` above); a full derivation of the remaining substrate primitive — the `κ₀ = χ(A)` trace-gap input inherited from `QouObstructionReductionContext` — remains pending, but is now LOCALISED rather than merely named: `QOU.AlgebraicSubstrate.ObstructionResidualGap` proves (i) that in the presence of `trace_pairing_cast` the three trace fields are equivalent to the single equation `κ₀ = χ(A)`, so the apparatus around it is decorative and `hattori_stallings` is the sole audit target; and (ii) that the two literature inputs (`vdb_duality`, `drinfeld_rigidity`) cannot reach it — an explicit structural core satisfies both while `κ₀ ≠ χ(A)` — although they do still force conclusion (a), `dim HH² = 1`. So closing this requires an actual Hochschild computation; no rearrangement of the existing fields will do it. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/collatz-contact-boundary.ts
theorem collatz_contact_boundary {R : Type*} [CommRing R]
    [ctx : CollatzContactBoundaryContext R] :
    (ctx.q_int_2 = 0 → kummer_obstruction_removable R) ∧
    ((2 : ℤ) ∣ ctx.chi_A) := by
  have h1 : (2 : ℤ) ∣ ctx.chi_A := by
    rw [ctx.chi_A_eq]; exact ⟨-3, rfl⟩
  exact ⟨fun _ => obstruction_removable_of_even_chi (R := R) h1, h1⟩

end QOU.AlgebraicSubstrate
