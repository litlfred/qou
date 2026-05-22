# Coordination ledger — λ_scale substrate-form falsification

**Goal:** Resolve the structural status of `conj:lambda-scale-substrate-form` for the Borromean baryon mass formula.

**Owner branch:** `claude/lambda-scale-conjecture-proof` (PR [#701](https://github.com/litlfred/qou/pull/701))

**Date opened:** 2026-05-18

## Scope map

| PR | Status | Classification | Relationship |
|----|--------|----------------|--------------|
| [#701](https://github.com/litlfred/qou/pull/701) | open | **own** | λ_scale falsification + Family A theorem |
| [#690](https://github.com/litlfred/qou/pull/690) | open | **overlap (constructive)** | Substrate-pure m_p, m_n via C2 + flavor-split — same goal, different framework |
| [#694](https://github.com/litlfred/qou/pull/694) | merged | dependency | Canonical-watcher baseline; §4b discipline rule; class-A banner pattern |
| [#683](https://github.com/litlfred/qou/pull/683) | merged | predecessor | Item B / Knot-fusion + my prior λ-scale audit work |
| [#696](https://github.com/litlfred/qou/pull/696) | open | tangent | Flavor-dressing functor (different scope, but uses CODATA validation aliases — flagged by canonical-watcher) |
| [#689](https://github.com/litlfred/qou/pull/689) | merged | predecessor | Operator-valued framework: vol-hyp 54→34 |
| [#715](https://github.com/litlfred/qou/pull/715) | merged | dependency | Class-A banner pattern I'm following |
| [#751](https://github.com/litlfred/qou/pull/751) | merged | **constructive sibling** | Workplan-0b/M_N routes A/B/C; explicitly flags "$d^2 A/da^2 = 0$ meaning" as open R&D piece |
| [#779](https://github.com/litlfred/qou/pull/779) (branch `claude/explore-d2a-categorical-8Eq2n`) | open | **resolves PR #751's open piece** | Audit doc + content edits propose the categorical meaning of $d^2 A/da^2 = 0$: golden Morse wall in $q$-moduli, not in $a$ |

## Findings

### PR #701 (own)

**Falsification of `λ_scale = 5/2 − h²·G + O(h⁴)`** via 5 independent structural routes:

1. **Family A (natural Wedderburn sum at H_4):** `(1/4) Σ_λ dim_q V_λ = (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)·h²`. Wrong sign and value vs `-G`. **PROVED in sympy + Lean (7 theorems).**
2. **Sign-flipped Wedderburn sums (32 variants):** exhaustive search; only all-positive preserves 5/2 leading; forces +3h²/4. No flip can produce negative h².
3. **Hecke level scan (H_2..H_7):** all natural normalisations give POSITIVE h² coefficients (H_2: 0, H_3: +5/32, H_4: +3/4, H_5: +25/13, H_6: +75/19, H_7: +6475/928).
4. **Transcendental ansätze:** Bloch-Wigner, Clausen Cl_2(π/k), ζ(3), Vol(4_1), Vol(B_3) basis — no integer relation.
5. **Single-knot K_p search:** no standard hyperbolic 3-manifold has Vol = 18.03 within 0.28% (closest: 9·Vol(4_1) at +1.35%).

**Canonical implication:** the framework's `prop:three-calibration-discipline` forbids CAL-4 baryon anchor (Option A from R&D 4 audit). Option B (single-knot K_p) is empirically ruled out. **Option C (treat as numerical coincidence)** is the only consistent path.

### PR #690 (sibling, OPEN)

Substrate-pure default for m_p / m_n:
- **m_p ← C2 inflection** = 938.918 MeV (+0.069% vs CODATA)
- **m_n ← m_p · (1 + (q−1)²·(1−q⁻⁴)·(1+ℏ_q³)/3)** = 940.212 MeV
- **Eliminates the calibration tautology** in `atomic_mass_via_rho_k.py` — CAL reduces to ONE input (m_e).
- Production output residuals are framework's actual predictive accuracy: p, n at +0.069%; D, T, ³He, ⁴He at +0.19%, +0.37%, +0.34%, +0.83%.

### PR #694 (merged, dependency)

Canonical-watcher baseline audit lists `lambda-scale-substrate-form` as "CANONICAL DERIVED at justification (5.4 ppm)" in §8a. **My PR #701 supersedes this** — the form is empirical only, not derived in any tested basis.

### `claude/explore-d2a-categorical-8Eq2n` (branch, no PR)

**Audit doc**: [`docs/audits/2026-05-18-d2a-categorical-thimble-resolution.md`](https://github.com/litlfred/qou/blob/claude/explore-d2a-categorical-8Eq2n/docs/audits/2026-05-18-d2a-categorical-thimble-resolution.md)

Five findings relevant to the λ_scale / m_p / C2-inflection thread:

1. **Color-tube cubic is $q$-independent** ($F \in \mathbb{Z}[z][c]$). $z_c$ and $H(z_c)$ are fixed complex numbers; the $d^2 S = 0$ wall must live in $q$-moduli, not $z$-plane. Rules out "saddle point of PL contour" as the meaning of $d^2 A/da^2 = 0$.
2. **Möbius $a(q)=(4-q)/(4q+3)$** has fixed points $q=1/\varphi,-\varphi$ from $q^2+q-1=0$ (golden node). $d^2 A/da^2 = 0$ at $a = a(q_0)$ is the archimedean reading of this algebraic wall via $\tau_q$.
3. **`conj:mobius-limit-from-thimble` Step 3 is unsupported** numerically — the actual descent re-entry is $z\approx 3.86$, not $0.388$. The Möbius value comes from the cubic's binomial $\binom{4}{1}=4,\binom{4}{3}=4,\deg_c F=3$, not steepest-descent geometry.
4. **`prop:sw-period-thimble-equivalence` A2.4** is mis-framed as Lefschetz decomposition; correct framing is Cauchy residue on $\mathcal{E}_q$ restricted to the principal Galois orbit $\{z_c^\pm\}$.
5. **Laurent-ring check** ($\mathbb{Z}[q^{\pm 1/2}, \zeta_5]$, with $\sqrt{5}\in\mathbb{Z}[\zeta_5]$): the Möbius $(4-q)/(4q+3)$ IS Laurent-compatible — contrary to "fails canonical form" judgment in PR #751's Route A table.

**Categorical-wall interpretation**: the C2 inflection on PR #690's categorical action $A(a)$ at $a = a(q_0)$ is the **archimedean specialisation** of the Morse-singular locus $\{q : q^2+q-1=0\}$ of the SW action $S_q$ on $\mathcal{E}_q$. PR #690's empirical 0.069% match is a section of the Möbius-wall family at $\tau_{q_0}$.

## Coordination actions

| When | Action | Where |
|------|--------|-------|
| 2026-05-18 | Posted coordination comment on #690 declaring constructive overlap, structural support for substrate-pure path | https://github.com/litlfred/qou/pull/690#issuecomment-4479405117 |
| 2026-05-18 | Updated `lambda-scale-substrate-form.md` with Class-A status banner + Family A theorem statement | `content/.../lambda-scale-substrate-form.md` |
| 2026-05-18 | Updated `lambda-scale-substrate-form.lean` with proved Family A theorems (7 closed-form theorems) | `content/.../lambda-scale-substrate-form.lean` |
| 2026-05-18 | Coordination comment from `claude/explore-d2a-categorical-8Eq2n` on PR #751 — proposes the categorical meaning of $d^2 A/da^2 = 0$ as the golden Morse wall ($q^2{+}q{-}1{=}0$ fixed points of the Möbius integration-limit pencil) | https://github.com/litlfred/qou/pull/751#issuecomment-4481902070 |

## Inconsistent findings

**Discovered inconsistency:** PR #694's baseline audit (§8a) classifies `lambda-scale-substrate-form` as "CANONICAL DERIVED at justification". My PR #701's exhaustive R&D shows the specific `5/2 − h²·G` form is NOT structurally derivable.

**Resolution:** Not an escalation-worthy contradiction — PR #694 explicitly says "justification" (not "derivation"), which matches my classification. The narrative on `lambda-scale-substrate-form.md` is updated to make the Class-A status explicit. The canonical-watcher framework's vocabulary (DERIVATION / JUSTIFICATION / NUMERICAL OBSERVATION / TAUTOLOGY) is exactly the right tool for this — my falsification merely strengthens the JUSTIFICATION classification to "PSLQ numerical coincidence, no structural backing".

## Next concrete task (non-overlapping)

Per the §6 escalation rules and the recognition that PR #690 is the structurally-correct path, my queue is:

1. **WAIT for PR #690 to merge** (don't duplicate substrate-pure m_p work).
2. **Address Gemini/Copilot reviews on #701** (high-priority: VOL_B3 standardisation, M_E from experimental_constants — DONE 2026-05-18).
3. **If #701 lands with #690 still open:** ensure narrative in `lambda-scale-substrate-form.md` cites #690's substrate-pure approach as the framework's mass-derivation path.

## Status

- PR #701: open, code-quality reviews addressed, R&D programme structurally complete.
- PR #690: open, substrate-pure default landed, awaiting merge.
- Coordination comment posted on #690 (no conflicts expected).
- No duplicate work between #701 and #690.
