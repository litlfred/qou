# Does a bar-odd part of the ruled Q_β trace carry the sinh role?

Bean `qou-hlx8` (epic `qou-qs0e`, tracker #7735). The owner said "work qou-hlx8".

* Lean: `folio/quantum-observable-universe/lean/QOU/QBeta/BarMarkovTrace.lean` (sorry-free)
* Probe (prints only, writes **no** witness, dashboard untouched):
  `computations/qbeta/qbeta_bar_odd_sinh_role_probe.py`, 8/8 checks.
* **Parallel effort.** Stream 12 (session_01Qmmkt8pE46F2YNM5QTVpHa, branch
  `claude/bar-parity-split-demote-2026-11-15`) is demoting `prop:bar-parity-split`. Its
  route 3 is this question, and the coordinator assigned it here. At the time of writing,
  that branch carries no route-3 computation (checked). `prop:bar-parity-split` and the
  complex-volume blocks are not touched here.

## 0. Result

**Scope-(a) negative: nothing structural motivates projecting Δ = n − p onto its bar-odd
part.** No symmetry that I tested sends the neutron word to the proton word. The bean's
anti-fit guard says the projection may only be used if such a motivation exists *before*
its value is computed. **So no Q_β value was computed from the projection, and none is
reported.**

What *is* established:

1. **The measured trace identity is now a theorem.** The earlier audit recorded
   tr^{z_D(q)}(bar Δ)(q) = tr^{z_D(1/q)}(Δ)(1/q), agreeing to 7e-52. It is explained by
   two facts:
   * `trM_barNF`: pulling the Markov trace back along bar gives the Markov trace at z − h,
     for **every** z.
   * `zD_bar_stable`: z_D(q⁻¹) = z_D(q) − h.

   Convention C, z = √q/(q+1), is **not** bar-stable (probe). So the bar-odd projection
   ½[f(q) − f(1/q)] is exactly the trace of the **element-level** bar-odd part
   ½(Δ − bar Δ). This is canonical as a projection, **under convention D only**.
2. **The only symmetries that make Δ odd are a grading, not an n ↔ p map.** The composites
   bar∘χ and χ∘bar send σ ↦ −σ and h ↦ −h, i.e. q ↦ −q. Here χ is the eigenline swap
   σ ↦ −σ⁻¹ from `qou-hlx6`. Under q ↦ −q every census letter (σ, σ − h/2, σ − h) is odd,
   so every 11-letter word is odd: S(n) = −n and S(p) = −p. Correspondingly
   tr^{z_D}(Δ) is odd in q. This is a word-length parity. It holds for any odd-length
   difference and says nothing about neutron versus proton.
3. **E₀ carries a sinh by itself.** The order-zero E₀ = m_e/(q(q − 1)) satisfies
   E₀(1/q) = −q³·E₀(q), i.e. E₀ = q^{−3/2}·m_e/(2 sinh(λ/2)) with λ = ln q.

## 1. Element level: which symmetry, if any, maps n to p?

Words: the γγ-selected `nuc11_interleaved` words built from the census letters
(core (σ₀σ₁⁻¹)³, then the quark tail, then the gluon σ₀σ₀). Every composite of up to four
of the following was tested exactly, at the NF element level and at the z_D trace level:

| symmetry | action | type |
|---|---|---|
| bar | σ ↦ σ⁻¹ = σ − h, h ↦ −h | Kazhdan–Lusztig bar involution |
| rev | reverse the word | anti-involution |
| swap | σ₀ ↔ σ₁ | diagram flip |
| χ | σ ↦ −σ⁻¹ = h − σ, same q | eigenline swap (`qou-hlx6`) |

| test | outcome |
|---|---|
| S(n) = ±p, for any composite S | **never** |
| tr^{z_D}(S n) = ±tr^{z_D}(p), for any S | **never** |
| S(Δ) = −Δ | only for S = bar∘χ or χ∘bar, and there S(n) = −n, S(p) = −p (§0 item 2) |

Why bar alone fails, at the letter level: bar swaps the u letter σ and the d letter
σ − h, and fixes the ud letter σ − h/2. Applied to the proton tail (u, ud, ud) it gives
(d, ud, ud). The neutron tail is (ud, ud, d): the **same multiset, in a different order and
on different generators**. The core and gluon are not bar-invariant either:
bar((σ₀σ₁⁻¹)³) = (σ₀⁻¹σ₁)³. So bar is a flavour flip on letters, but it does not carry the
proton word to the neutron word.

**Scope (a).** The exclusion covers the composites of these four symmetries on these
words. A symmetry outside this set, or a different word pair, is not excluded. So
"the sinh role is carried by a bar-odd part" is **not motivated**, but it is not refuted.

## 2. Trace level (Lean, sorry-free)

Work on the NF free module of H₃ (`mulNF`, `trM`). The map `barNF h` sends σ_g ↦ σ_g − h.

| theorem | statement |
|---|---|
| `barNF_one`, `barNF_gen0`, `barNF_gen1` | unit ↦ unit, σ_g ↦ σ_g − h |
| `barNF_mul` | barNF h (u ·₋ₕ v) = barNF h u ·ₕ barNF h v: a ring map H₃(q⁻¹) → H₃(q) |
| `trM_barNF` | trM z h (barNF h v) = trM (z − h) (−h) v, for every z |
| `zD_bar_stable` | z_D(q⁻¹) = z_D(q) − (q − q⁻¹), given q ≠ 0 and q² + 1 ≠ 0 |
| `trM_barNF_zD` | under z_D, the pulled-back trace is the z_D trace at q⁻¹ |

`#print axioms` on all five: `[propext, Classical.choice, Quot.sound]`. Generic
`CommRing` / `Field`; no ℝ.

Consequence: the function f(q) := tr^{z_D(q)}(Δ)(q) satisfies
f(1/q) = tr^{z_D(q)}(bar Δ)(q). So

  ½[f(q) − f(1/q)] = tr^{z_D}(½(Δ − bar Δ)).

The bar-odd projection of the trace is the trace of an algebra element. This is a property
of convention D, and it is the strongest positive statement available: if a structural
reason for "Q_β reads the bar-odd part of Δ" were found, convention D would make that
reading consistent at the trace level. No such reason was found (§1).

The exact parts, recorded in the previous audit and unchanged:
* bar-even part of f: −h²·[2]_q·(q² + q⁻²)/8;
* bar-odd part of f: (q² − 1)(q⁴ + 1)·P′(q)/(8q⁷(q² + 1)²).

They are recorded as functions. No CODATA comparison is made.

## 3. Which factor would carry the parity

E₀(1/q) = −q³·E₀(q) exactly (probe check). Equivalently, q^{3/2}·E₀ = m_e/(2 sinh(λ/2))
is exactly bar-odd. So in Q_β = |tr|·E₀, a sinh is already present in the energy scale, at
half argument and up to q^{3/2}. Neither factor is bar-odd as written. Symmetrising E₀ to
make the product bar-odd would be inventing a normalisation, and it is not done. The
canonical tower-summed E₀ has the extra factor 1/(1 − ℏ_q²), with ℏ_q = 1 − q⁻¹; that
factor is not analysed here.

## 4. Scope of every negative

* "No tested symmetry maps n ↔ p": **(a)**. The set tested is the composites of
  {bar, rev, swap, χ} up to length 4.
* "The bar-odd projection is not structurally motivated by Δ": **(a)**. It follows from the
  previous line.
* "The only Δ-odd symmetry is the length parity q ↦ −q": **(a)** within the same set.
  Within that set the parity statement itself is exact: every census letter is odd in
  (σ, h).

## 5. Owner decisions

### D-H8a: keep pursuing "Q_β reads the bar-odd part"?

* **(A) Close the route as unmotivated.**
  * *Means:* record §1 as the answer, and drop route 3 from stream 12's list.
  * *Costs:* none.
  * *Risks:* a symmetry outside the tested set might exist.
  * *Commits to:* the bar-odd part is not a Q_β candidate unless such a symmetry is
    exhibited.
* **(B) Search further for an n ↔ p symmetry.**
  * *Means:* widen the search to word-dependent maps, for example flavour flip on the tail
    only, composed with a core automorphism.
  * *Costs:* hours.
  * *Risks:* a map tailored to send this n to this p is selection against the target unless
    it is defined independently of the words.
  * *Commits to:* a definition of the map before testing it.

**Default if nothing is said: (A).** **Recommendation (judgement): (A).** The tested set
already includes every algebra-level involution the corpus names, and a word-dependent map
is exactly the selection the guard forbids.

### D-H8b: is the bar-stability of z_D worth stating in the convention-D content?

* **(yes)**
  * *Means:* one sentence in a convention-D content block citing `zD_bar_stable` /
    `trM_barNF`.
  * *Costs:* a small content edit plus render-QA.
  * *Risks:* none to numbers.
  * *Commits to:* nothing beyond the proved identity.
* **(no)** Keep it in the Lean file and this audit only.

**Default: (no).** **Recommendation (judgement): (yes).** It is a short, exact,
convention-distinguishing fact (C fails it), and it is the reason the earlier measurement
came out at 7e-52.
