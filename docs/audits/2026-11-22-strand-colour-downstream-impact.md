# Strand colour states: downstream impact map (2026-11-22)

Working assumption (owner, 2026-11-22, `owner-rulings.md`): the three states of a strand are the
three colours. Colour is true Hopf `U_q(gl₃)` at generic `q`, carried by the tensor braiding
`X = Ř_colour · Ř_flavour`, with the gl₆ coideal as cross-check. Issue #9106, PR #9107.

This is a map, not a recomputation. No measured value enters any Lean file named here; the
comparison points are named only to say which ones would move.

## 1. What is proved (all sorry-free, `lean`-direct exit 0)

| Statement | Lean |
|---|---|
| `X` satisfies the cubic `(X − q²)(X + 1)(X − q⁻²) = 0`, and is not Hecke in general | `HopfColourTensorBraid.tensor_braid_cubic(_of_commute)`, `tensor_braid_not_hecke` |
| Jimbo's `Ř` for gl₃ is Hecke and braids on `(K³)^{⊗n}` | `JimboGl3Singlet.hecke`, `braid` |
| `Ř` commutes with `ΔE_i`, `ΔF_i`, `ΔL_j` (colour is a Hopf action that commutes with the braid) | `JimboGl3Singlet.comm_E`, `comm_F`, `comm_L` |
| Both braid generators act on `ε_q` by `−q⁻¹`; `ε_q` spans the `q`-determinant line | `R12_eps`, `R23_eps`, `E_eps`, `F_eps`, `L_eps` |
| For `q² + 1 ≠ 0` the colour singlet is one-dimensional | `singlet_unique` |
| On singlets `X = −q⁻¹·b`, and `−q·X = b` is the flavour Hecke generator; under convention D the `(1³)` weight is 0 | `singlet_hecke`, `singlet_rescale`, `singlet_threeRow_eq_zero_of_conventionD` |
| A braid word in `X` equals `(−q⁻¹)^{e}` times the same word in `b`, `e` = exponent sum; same for any linear trace | `ColourSingletDownstream.word_eval_smul`, `trace_word_smul` |
| Coideal singlet generator `−b⁻¹` and tensor generator `−q⁻¹b` multiply to `q⁻¹` | `coideal_mul_tensor` |
| Read in raw `X`, the p–p bond factor is `−q²/(q²+1) < 0` for real `q > 0` | `raw_pp_factor` |

## 2. The one choice that decides every downstream number

On the singlet sector there are two natural generators: the raw strand braid `X`, and the
rescaled `−q·X = b`. The Lean above says exactly what each choice does.

* **Rescaled generator `−q·X` (reading "D up to the mirror").** Every flavour formula is unchanged
  term by term, because `−q·X` *is* `b`. Nothing in production moves.
* **Raw generator `X`.** A word with exponent sum `e` gains `(−q⁻¹)^{e}`. Linear combinations do not
  scale uniformly, because `X` obeys a different quadratic on singlets (`X⁻¹ = −q·b⁻¹`).

## 3. Consumers, by quantity

Located by reading the producers; file:line references are to `main` at 5274f30be.

| Quantity | Word(s) traced | `e` | Rescaled `−q·X` | Raw `X` |
|---|---|---|---|---|
| `m_p/m_e` (`m_p_substrate_identity_50dps.py:129-205,346`; `canonical_mass.py:15-23`) | `β_Bor = (σ₀σ₁⁻¹)³`, as Jones `V(𝓑₃)/[2]²` | 0 | unchanged | unchanged |
| `Q_β` (`derived_masses.py:608-642`) | `V³ = (σ₀σ₁⁻¹)³` (γγ selection forces writhe 0) | 0 | unchanged | unchanged |
| `Δ_pn = m_n − m_p` (`m_p_substrate_identity_50dps.py:359`, `= Q_β + m_e`) | inherits `V³` | 0 | unchanged | unchanged |
| Half-life weak vertex `W(q) = tr_M((σ₀σ₁)⁵)` (`markov/weak_vertex_t35_trace.py:3,73`) | `(σ₀σ₁)⁵` | 10 | unchanged | gains `q⁻¹⁰` |
| Per-bond binding `B = E₀ Σ log(1/f)` (`derived_bond_graph_binding.py:8-34`, `closed_form_tau_M.py:229-243,365-402`) | p–p `σ`, n–n `σ⁻¹`, p–n `σ − h(½ − δ/4)` | +1, −1, mixed | unchanged | p–p factor negative (`raw_pp_factor`): the log law has no real value |
| ⁴He γγ bond chain (`docs/audits/2026-11-22-sign-conventions-table.md:40-44`) | `σ_iσ_{i+1}⁻¹` | 0 | unchanged | unchanged |
| Photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` | `σ₀`, `σ₁`, `σ₀σ₁⁻¹` | 1, 1, 0 | unchanged | `φ₀, φ₁` absorb `−q⁻¹`; constant 1 and `φ₀₁` term unchanged |
| `m_μ/m_e = Vol(4₁)/ℏ_q²` | no trace | — | unchanged | unchanged |
| Electron `σ₀σ₁σ₀` | no production trace found | 3 | — | would gain `−q⁻³` |

Not checked: whether the charge insertions `Q_ij` in the two-term trace
(`canonical_mass.py:249-264,352-366`) are braid elements; if they are, they need their own
exponent sums.

## 4. What this means for the comparison points

On the rescaled reading the working assumption changes no model number: `m_p/m_e`, `Δ_pn`, `Q_β`,
binding and the half-life are the same closed forms. What it adds is structure: colour is now a
genuine Hopf symmetry of every hadron trace, and the baryon is its unique singlet.

On the raw reading, the only words that move are those with `e ≠ 0`. The two production places
that carry such words, the per-bond binding factors and the half-life weak vertex, both move, and
binding stops being defined. That is a scope-(a) negative for the raw reading as it stands, not a
structural exclusion: a bond law written for `X`'s own quadratic was not attempted.

## 5. Open

* Owner choice between the rescaled and raw generators (asked 2026-11-22).
* Owner confirmation that "Barry" means baryon.
* Leptons: under the assumption a lepton strand is coloured too; which colour sector the electron
  occupies is not fixed by anything above.
