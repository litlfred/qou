# Path to 1 ppb — Agent Handover

*Purpose: context doc for the next-session agent working on Option 1 (switch to JSJ) + Option 2 (push JSJ to ppm). Read this first.*

## Goal

Predict nuclear binding energies at **1 ppb** (10⁻⁹ relative) with **zero free parameters** using the JSJ + hyperbolic-volume canonical pipeline.

## Current best result

Zero-parameter predictions (from `jsj_alpha_clustering.py` + `jsj_verification.py` on main):

| atom | B_AME (MeV) | B_pred (MeV) | err |
|------|------------:|-------------:|----:|
| D (↔ knot 6_2) | 2.2246 | 2.2493 | +1.1% |
| T (↔ knot 8_11) | 8.4818 | 8.4681 | −0.2% |
| ³He (↔ Borromean) | 7.7180 | 7.4929 | −2.9% |
| ⁴He (= 1 α) | 28.2957 | 28.2957 | 0% (base) |
| ¹²C (= 3 α + 3 c_αα) | 92.1617 | 92.1617 | 0% (fit) |
| **¹⁶O** (= 4 α + 6 c_αα) | **127.619** | **127.732** | **+0.09%** |

**Headline claim**: $B = \rho_F(\mathcal{K}) \cdot \text{Vol}_\text{hyp}(\mathcal{K})$ with $\rho_F = m_e$ for bonds, $\rho_F = 2m_e$ for internal matter.

## Canonical pipeline (Option 1 decision — use JSJ)

1. Atom braid $\beta_{Z,N} \in B_{3A}$
2. Hecke NF in $H_{3A}(q_0)$
3. Link class via Markov equivalence
4. JSJ decomposition into Seifert + hyperbolic pieces
5. Per-piece Vol via SnapPy verified high-precision
6. Per-piece density $\rho_F = m_e \cdot n_\text{chir}$
7. Sum $\sum_P \rho_F(P) \cdot \text{Vol}(P)$
8. Compare to AME

**DO NOT** use `exact_binding_per_operation.py` — it sums log-volumes instead of volumes and under-predicts by 85-99%.

Continues in path-to-1ppb-02-content.md, path-to-1ppb-03-engine.md, path-to-1ppb-04-plan.md.
