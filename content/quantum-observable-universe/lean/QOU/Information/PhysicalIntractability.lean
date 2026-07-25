import Mathlib.Tactic

/-!
# QOU.Information.PhysicalIntractability — the honest, derived lower bound

The one route by which Option B yields a **derived** (non-fiat) separation —
though of something strictly weaker than abstract `P ≠ NP`.

The corpus's **Bekenstein / bandwidth bound** says a substrate computation
processes at most `𝔅(q)` q-bits per Planck step, so in `t` steps it can access
at most `t · 𝔅` bits.  If *deciding* an instance of size `n` genuinely requires
`info(n)` bits of the degree-0 obstruction, then a correct bandwidth-limited
device needs at least `info(n) / 𝔅` steps.  When `info(n)` is super-polynomial,
**no bandwidth-limited device decides the problem in polynomial time**.

This is a genuine information-theoretic lower bound — a pigeonhole argument,
proved sorry-free below — **not** a fiat identification.  Its honest scope:

* the physical input is `info(n)` super-polynomial (the degree-0 answer needs
  more than poly bits — the horizon/`3^c`-tree content, to be *derived*, not
  assumed);
* the conclusion bounds only **bandwidth-limited (physical)** computation.  A
  general Turing machine is not Bekenstein-limited, so this is **strictly
  weaker than abstract `P ≠ NP`** — a *physical Church–Turing* statement, not
  the Clay problem.

That is the ceiling of the non-fiat route, and it is the theorem the QOU is
actually positioned to prove.
-/

namespace QOU.Information

/-- **Steps lower bound (sorry-free).**  A bandwidth-`B` device that in
    `steps n` steps accesses at most `steps n * B` bits, and is *correct*
    (accesses at least the `info n` bits needed to decide instance size `n`),
    must run for at least `info n / B` steps. -/
theorem steps_lower_bound (B : ℕ) (hB : 0 < B) (info steps : ℕ → ℕ)
    (correct : ∀ n, info n ≤ steps n * B) (n : ℕ) :
    info n / B ≤ steps n := by
  calc info n / B ≤ steps n * B / B := Nat.div_le_div_right (correct n)
    _ = steps n := Nat.mul_div_cancel _ hB

/-- A function `f : ℕ → ℕ` is **super-polynomial** if it eventually exceeds
    every polynomial `c · n^k`. -/
def SuperPolynomial (f : ℕ → ℕ) : Prop := ∀ c k : ℕ, ∃ n, c * n ^ k < f n

/-- **Physical intractability (sorry-free).**  If the information required to
    decide `L` (per bandwidth unit, `info n / B`) is super-polynomial, then the
    step count of *any* correct bandwidth-`B` device is super-polynomial too —
    i.e. no bandwidth-limited device decides `L` in polynomial time.

    A **derived** lower bound (pigeonhole on the bandwidth bound), not a fiat.
    Scope: bandwidth-limited computation only — strictly weaker than abstract
    `P ≠ NP`. -/
theorem no_poly_bandwidth_decider (B : ℕ) (hB : 0 < B) (info steps : ℕ → ℕ)
    (correct : ∀ n, info n ≤ steps n * B)
    (hinfo : SuperPolynomial (fun n => info n / B)) :
    SuperPolynomial steps := by
  intro c k
  obtain ⟨n, hn⟩ := hinfo c k
  exact ⟨n, lt_of_lt_of_le hn (steps_lower_bound B hB info steps correct n)⟩

/-- **Super-polynomiality lifts through a lower bound (sorry-free).**  If
    `g ≤ f` pointwise and `g` is super-polynomial, so is `f`. -/
theorem SuperPolynomial.of_le {f g : ℕ → ℕ} (hg : SuperPolynomial g)
    (hle : ∀ n, g n ≤ f n) : SuperPolynomial f := fun c k =>
  (hg c k).imp fun n hn => lt_of_lt_of_le hn (hle n)

/-- **Exponential information ⇒ physical intractability (sorry-free).**  The
    concrete QOU case: if deciding size-`n` instances requires (per bandwidth
    unit) at least the `2^n` bits of the full degree-0 obstruction, and `2^n`
    itself is super-polynomial, then no bandwidth-limited device is
    polynomial-time. -/
theorem no_poly_bandwidth_decider_of_exp (B : ℕ) (hB : 0 < B)
    (info steps : ℕ → ℕ) (correct : ∀ n, info n ≤ steps n * B)
    (hexp : ∀ n, 2 ^ n ≤ info n / B)
    (hexp_superpoly : SuperPolynomial (fun n => 2 ^ n)) :
    SuperPolynomial steps :=
  no_poly_bandwidth_decider B hB info steps correct
    (hexp_superpoly.of_le hexp)

end QOU.Information
