# RESULT — colour in the full Hecke tower (bean `qou-ni4b`)

Owner question (verbatim): *"What about looking in the full Tower for the color"*.

- Pre-registration: `PREREGISTRATION-colour-full-tower.md`, commit `e16afb61a6d` (16:55 UTC), pushed
  before the probe existed.
- Probe: `qcd_colour_full_tower_probe.py`; output: `qcd_colour_full_tower_probe.out.json`.
- **27/27 checks pass.**
- Exact sympy over ℚ(q) and exact integers. No float, and `q₀` is not used.

**Commit attribution.** The probe and its `.out.json` landed in commit `c3f1b05557a`
(17:12 UTC). That commit belongs to the sibling spin-factor agent, which shares this worktree
and staged them by sweeping. That commit is the final 27/27 version, byte-identical to the one
reported here, and it comes after the pre-registration. So the order *pre-register, then
compute* holds; only the commit author is off.

## Claim

The full tower does carry colour, but convention D cannot see it.

- On `(ℂ³)^⊗n`, the full Hecke tower has `U_q(gl₃)` as its Schur–Weyl commutant. This colour
  action meets (a), (b), (c) and (f).
- Every Markov trace on that colour module, i.e. every diagonal twist `K` making
  `x ↦ tr(K^{⊗n}x)/(tr K)^n` Markov, has `z` fixed by the rank of `K`:

  | rank K | z | which trace |
  |---|---|---|
  | 1 (3 supports) | `q` | level 1 |
  | **2 (3 supports)** | **`q³/(q²+1)` = z_D** | **convention D** |
  | 3 | `q⁵/(q⁴+q²+1) = q³/[3]_q` | level 3 |

- The **only** `U_q(gl₃)`-invariant twist (the pivotal element) is the rank-3 one,
  `diag(q⁻⁴, q⁻², 1)`, up to scale.
  - Convention D is realised on the colour module only by a **singular** twist. That twist
    annihilates one colour direction.
  - The z_D twist with support {1,2} leaves the trace functional invariant under
    `E₁, F₁, K₁, K₂` only, i.e. `U_q(gl₂) × U(1)`.
  - So **(d) fails structurally.** Reading D as a colour trace breaks SU_q(3) to U_q(2).
- **The colour singlets of the whole tower sit inside D's radical.**
  - The `U_q(sl₃)`-singlet sector of `(ℂ³)^⊗3A` is the Specht block of the rectangle `(A,A,A)`.
    The probe checks this explicitly at `n = 3` (singlet space 1-dimensional, `σᵢ = −q⁻¹`).
  - That block has three rows, so D's weight on it is identically zero, for every baryon
    number A.
  - Scope (b). Invariant: `ocneanuWeight_conventionD_eq_zero_of_three_rows`.
  - Answer to the owner's question: **the colour is in the full tower, and convention D puts
    every colour singlet in its radical.** This is T4 confirmed.

## Per candidate

| | result | scope |
|---|---|---|
| **T1** Schur–Weyl dual on (ℂ³)^⊗n | `U_q(gl₃)` commutes with Ř and is compatible with H_n ⊂ H_{n+1}. Meets (a)(b)(c)(f). Markov twists: rank r ⇒ z_r (table above). The invariant twist is unique, and it is z₃. D needs a singular twist whose stabiliser is U_q(gl₂)×U(1). **(d) fails.** | (b) within diagonal twists. Invariant: the kernel of an invariant twist is a submodule of the irreducible ℂ³, hence 0; computed: the invariant-twist space is 1-dim and invertible. |
| **T2** relative commutants `H_{n−k}' ∩ H_n` | Depth 2: blocks of size ≤ 2, both towers, n ≤ 9. Depth 3: full Hecke has block sizes {1,2,3,6} (n ≥ 6); D/TL has {1,2,3} (n ≥ 4). So an `M₃` block, hence a derived `sl₃`, appears at depth 3 in both towers. This is a pre-declared coincidence (§4): it is the generic box+domino skew shape. **(b) fails structurally**: anything in H_n that commutes with every σᵢ is central, and Z(H_n) is commutative. | (b). Invariant: centre commutativity. Beyond what `ThreeStrandColourTowerCP` shows for n = 3, this holds for all n. |
| **T3** ℤ₃ / period 3 | (i) `V = σ₀σ₁⁻¹` on (2,1) has char. poly `t² + (1+h²)t + 1`, det 1. `V³` is scalar there iff `h²(h²+2) = 0` (V³ off-diagonal = `−(q−1)²(q+1)²(q⁴+1)/q⁴`). So ℤ₃ holds only at h = 0 (q = ±1) or h² = −2. Never at real q > 1. (ii) Graph automorphisms, levels < 9: Young's lattice has {id, transpose}; the two-row (D) lattice is trivial. No ℤ₃. (iii) D weights `[n−2k+1]_q/[2]_q^n` depend only on n−2k; no period 3 in A. | (i) exact over ℚ(q), all orders in q. (ii)(iii) are finite checks (levels ≤ 9), scope (a) beyond that. |
| **T4** three-row data in a non-trace part | The D radical is the sum of all three-row blocks, dim `n! − Catalan(n)` (1, 10, 78, 588, 4611, 38890, 358018 for n = 3..9; matches `qou-8iru`). Colour singlets `(A,A,A)` have f = 1, 5, 42, 462 for A = 1..4, all inside the radical. **Confirmed.** | (b). Invariant as above. |

## What is established and what is not

Established:

- On the colour module `(ℂ³)^⊗n`, convention D is exactly the colour-twisted trace with a
  rank-2 twist.
  - This is an exact identity over ℚ(q): Markov holds on all `T_w` for n = 1, 2; the trace
    property holds on H₃; `y_λ = s_λ(K)/(tr K)^n` equals D's closed form for every λ, n ≤ 9.
  - Ocneanu uniqueness (a Markov trace is fixed by z) extends this to the whole tower.
- D is therefore the colour trace that "forgets one colour". No colour-invariant twist gives z_D.

Not established:

- Twists that are not diagonal, and traces of the form `tr(Z_n ·)` with `Z_n` a non-grouplike
  central element of the commutant.
  - Such `Z_n` can reproduce D's weights while staying `sl₃`-invariant, by putting coefficient 0
    on the three-row blocks. But that is choosing a per-n element to match the target, i.e.
    selection. It was not pursued.
- Colour modules other than `ℂ³` (e.g. ℂ³ ⊗ flavour; see `qcd_colour_action/` K0–K4).
- No gluon is identified. No Lean was added: every proved invariant cited already exists in the
  corpus, and the new statements are finite exact computations.

## Post-hoc surprises (labelled)

1. **Post-hoc, a correction to my own pre-registered test.** The pre-registration wrote the
   Markov twist condition as `tr₂((1⊗K)Ř) = s·Id`. The correct condition is `PK = sK`, i.e.
   scalar on the range of K, because cyclicity places a K on the last factor.
   - Under the pre-registered (too strong) condition, only the rank-3 twist survives, and the
     rank-2 z_D twist was reported missing (first run).
   - The registered prediction "rank-2 twists give z_D" holds under the correct condition. The
     condition, not the prediction, is what changed.
2. **Post-hoc.** The non-adjacent support {1,3} also gives z_D (`K = (q⁻³, 0, q⁻¹)`), not only
   {1,2} and {2,3}. Since its Schur weights equal the {1,2} ones, the trace is the same.
3. **Post-hoc.** The unique `U_q(gl₃)`-invariant twist `diag(q⁻⁴,q⁻²,1)` coincides, up to scale,
   with the rank-3 Markov twist `(q⁻⁵,q⁻³,q⁻¹)`. In this setting "colour-invariant" and
   "level 3" are the same condition. This is standard (the pivotal trace is the quantum trace),
   but here it was computed rather than assumed.

## Implications

- The N = 2 vs N = 3 tension is now an exact statement. The single object `(ℂ³)^⊗n` carries
  both the level-3 trace (colour-invariant, z₃) and convention D (z_D). The two differ exactly
  by whether the twist is invertible.
- Choosing D is choosing a trace that annihilates the colour determinant line, and with it every
  colour-singlet baryon sector `(A,A,A)`.
- This sharpens `qou-ezhi` ("the substrate has no colour singlet"): the colour singlets are not
  absent from the tower; D puts them in its radical.
- What would close the gap is not in the corpus. It would be an object on which D is a
  colour-invariant functional, which T1 excludes for diagonal twists on ℂ³; or a decision that
  colour observables are read through the level-3 trace, not through D.
  - The second is a modelling choice for the owner.
  - The 2026-10-10 test (`qou-lxh5`) already found the level-3 substitution in the proton
    identity about 1100× worse, scope (a).

## Verification

- `python3 -u qcd_colour_full_tower_probe.py` → `SUMMARY 27/27`, exit 0.
- `scripts/precision-gates.sh --changed`: no gate names any file in this directory. The RED
  lines it prints are repo-wide ratchets, and the modified audit witnesses were already in the
  tree before this work (not staged, not committed).
