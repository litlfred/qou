# Four-term chiral photon in place of the single-crossing photon (2026-11-20)

The owner ruled (Carl, 2026-11-18, confirmed 2026-11-20; bean `qou-99qc`) that `def:photon` is
γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹. The owner added at 16:34: *"make sure using the correct four-term photon that has the
chirality part"*. Producer `photon_chiral_ports_probe.py` (helper `h3_photon.py`), witness
`photon-chiral-ports.witness.json`, 9/9 checks pass. The arithmetic is exact over ℚ(q) and the values are taken at the proton q₀,
70 dps, with convention D. The only colour weights evaluated are the corpus-derived eigenvalue pair γ₊ = γ(0,0,qh),
γ₋ = γ(0,0,−q⁻¹h), for which V³ = γ₊γ₋ (`borromean-two-photon-factorisation`). All other weights stay
symbolic. Nothing is fitted.

## A. `knot-operator-table.py` key table (audit C6; the record took photon = σ₀)

tr_M at q₀, record σ₀·T·σ₀ → four-term γ₊·T·γ₋ (γ₋·T·γ₊ gives the same trace):

| T | record | γ₊Tγ₋ | e⁻ term, record → new |
|---|---|---|---|
| T₁,₀ | 1.128088744 | 0.998562164 | no → no |
| T₂,₁ | 0.848526607 | 0.605509828 | no → **yes** |
| T₂,₂ | 1.305481970 | 1.125150229 | no → **yes** |
| T₂,₃ | 0.799853186 | 0.691166478 | yes → yes |
| T₂,₅ | 0.943498443 | 0.807031395 | yes → yes |

With symbolic weights the e⁻ coefficient of γ(φ)·1·γ(ψ) is φ₀₁ψ₀ + φ₁ψ₀₁. It needs the vertex term on one photon
and a chiral single-crossing term on the other.

## B. `gram-matrix-dual.py` (audit C5)

- The labelled fits 0.0487 (linear) and 0.0978 (circular) are three-term, φ₀₁ = 0. They are the **same element in both charts**,
  so the ruling does not move them. They remain fits (audit C2), shown only as a labelled comparison.
- The "bare photon pair σ₀²" (tr_M = (q⁴+1)/(q²+1) = 1.128088744) is not a photon pair under `def:photon`.
  Two bare photons give γ(0)γ(0) = 𝟏 (tr_M = 1). The eigenvalue pair gives γ₊γ₋ = V³,
  tr_M = −(q¹²−3q¹⁰+2q⁸−4q⁶+2q⁴−3q²+1)/(q⁴(q²+1)²) = 0.998562164, χ_sym = χ_alt = 1.
- The witness row `particles.photon` = 𝟏 is the bare photon. It is consistent with the ruling, and its numbers are unchanged.

## C. `gamma_gamma_pair_production_decomposition.py` (audit C7)

β_Bor = V³ = γ₊γ₋ holds exactly, and the factors commute. It is **two four-term photons**. The record reading was
three γγ̄ events with photon = σ₀ and anti-photon = σ₁⁻¹. Under the ruling V = σ₀σ₁⁻¹ is one photon's fourth term. tr_M(β_Bor),
and every Markov-trace number in that producer, are properties of the braid, so they do not move.

## D. `breit_wheeler_filtration_chain_probe.py` (audit C9)

The promote/split rule is a statement about single generators, and it survives as a statement about the σ-**terms** of the
photon. It does not transfer to the photon itself:

- One pure-vertex photon γ(0,0,φ₀₁) already occupies grades 0, 1 and 2, because V = σ₀σ₁ − hσ₀. A photon is not grade-homogeneous,
  so "a photon promotes the grade by one" is false for the four-term photon.
- γ(φ)γ(ψ) reaches grade 3 (e⁻) only through φ₀₁ψ₀ + φ₁ψ₀₁.
- At the eigenvalue pair the product is V³, which lives in grades 0–2 and has **no e⁻ term**.

## E. `sdp_gamma_gamma_to_qqbar.py`

The scaffold is H₂, with photon = the σ₀ slot. The chiral vertex needs σ₁, so the four-term photon lives in H₃. At q₀ the
symmetric parts of all three Wedderburn blocks of γ₊, γ₋ and γ₊γ₋ are PSD. The characters (sym / std / alt) are:
γ₊ 1.23205 / 1.75781 / 1.23205, γ₋ 0.81165 / 2.19658 / 0.81165, and γ₊γ₋ 1 / 1.99419 / 1. The H₂ demo numbers are
unchanged and remain an H₂ statement.

## F. The γγ unit under every V-word probe

Every V-word alphabet (`qbeta_gamma_gamma_*`, `band_gamma_gamma_vertex_*`, `gg_four_strand`, `h2_*`,
`gg_twist_reading3`, `gg_decay`, `gg_two_orientations`, `photon_electron`) is the **φ₀ = φ₁ = 0
specialisation** of products of four-term photons (check F). V³ = γ₊γ₋ is the eigenvalue-pair product. These alphabets drop the chiral
single-crossing part φ₀σ₀ + φ₁σ₁. At the only corpus-derived weights that part is zero, so the
V-word results **are** the four-term photon at those weights. The part is not inert, though. At the eigenvalue pair the first-order
sensitivities at q₀ are:

| | ∂/∂φ₀ | ∂/∂φ₁ | ∂/∂ψ₀ | ∂/∂ψ₁ |
|---|---|---|---|---|
| tr_M | 0.52693 | 0.49729 | 0.71835 | 0.75486 |
| χ_sym | 0.90092 | 0.90092 | 1.36755 | 1.36755 |
| χ_std | 0.28953 | 0.16968 | 0.10991 | 0.25757 |
| χ_alt | −0.73123 | −0.73123 | −1.10998 | −1.10998 |

So any nonzero chiral part moves the traces and the selection characters at first order. The corpus has no derived
value for φ₀, φ₁, and choosing one would be a fit. Both statements hold: the V-word results stand at the derived
weights, and they are not robust to a chiral part. The Borromean Q_β case under these weights is #8586 arm γ
(Q_β = 0 for every linear ε). It is cited here, not redone.

## G. `tbl:four-term-pair-nucleon-table1-data` (producer and weights unrecorded)

No producer or witness exists for this table. The witness it would cite, `breit-wheeler-nucleon-nf.witness.json`, is
absent, and no script in `computations/` emits it. I reconstructed the weights instead: the straight-chart square
γ_straight(a,a,b)² with **a = 0.0487** (the Breit–Wheeler linear *fit*) and **b = 0.02** (no source found)
reproduces all six rounded entries to rounding (check G). The same weights with the ruled photon, at q₀:

| | record | straight chart (reconstructed) | ruled photon, same weights |
|---|---|---|---|
| 1 | 1.005 | 1.0047433 | 1.0043536 |
| σ₀ | 0.099 | 0.0988698 | **0.0904259** |
| σ₁ | 0.099 | 0.0988698 | 0.0987862 |
| L₊ | 0.043 | 0.0427789 | 0.0425578 |
| L₋ | 0.003 | 0.0027716 | 0.0025680 |
| e⁻ | 0.002 | 0.0020316 | 0.0019480 |

The visible change is the σ₀ entry, which moves by −hφ₀₁ (the vertex's σ₀ part). The two σ coefficients are no longer
equal. Both weights are a fit or unsourced, so neither column is a derived result. I have not edited the table. Whether to
restate it, and with which weights, is an owner call.
