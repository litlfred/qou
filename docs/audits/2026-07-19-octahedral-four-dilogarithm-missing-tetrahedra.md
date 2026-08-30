# The missing 3 dilogarithms = the octahedron's other 3 tetrahedra (the −9% closure lead)

**Date:** 2026-07-19 · **Branch:** `claude/nastokes-higher-order-eunit-2026-07-19` (PR #4127) ·
**Axis:** Δ_λ binding magnitude — the μ₀ −9% closure · **Owner steers:** *"the other 3
dilogarithms — what do they correspond to? is it what happens w.r.t. the alien derivative? how
does that impact mass or binding compute?"* **Tier:** structural finding + hypothesis (scope-(a);
no fit; nothing wired).

## 0. The setup

Merged #4117: `E_unit`'s source is the counit — `μ₀ = m_e/(3(q−q⁻¹)/2)`, the **first-order**
per-crossing phase, deuteron −9.2%. The owner uploaded three papers (`math-ph/0012035` NA-Stokes,
`2509.02354` q-dilog holonomy, `phys-rep09` Magnus) as the source material for the higher-order
closure.

## 1. The finding (solid — the paper's theorem)

`2509.02354` (McPhail-Snyder–Reshetikhin, *The holonomy braiding for `U_ξ(sl₂)` in terms of
geometric quantum dilogarithms*): the holonomy R-matrix of quantum `sl₂` at a root of unity
**factorizes into a product of four quantum dilogarithms**, and **each crossing braiding
corresponds to a twisted ideal octahedron** whose **4 dilogarithms are its 4 ideal tetrahedra**
(operators `Z_b, Z_t, Z_r, Z_l` — bottom/top/right/left). This is the **octahedral decomposition**:
each crossing's complement = one ideal octahedron = 4 ideal tetrahedra, parameters = hyperbolic
structures.

**So: the QOU uses a *single* Faddeev `Φ_q` per crossing = *one* tetrahedron. The "missing
something" is literally the other 3 tetrahedra of the crossing's octahedron.**

## 2. The alien-derivative connection (owner steer — solid)

The 4-dilogarithm octahedral **state-integral is resurgent**: its asymptotic expansion carries
**Stokes constants / alien derivatives** whose contributions are the tetrahedron faces
(Garoufalidis–Gu–Mariño 3d-index — the same machinery as sibling **#3805**'s `A_ω` Stokes constant
on `4₁`). So the **missing 3 dilogarithms ≡ the alien/Stokes (lateral) completion** of the single,
perturbative (median) `Φ_q`. The binding −9% and the keystone `A_ω` are plausibly the **same
object** viewed from binding vs. resurgence.

## 3. Impact on mass vs binding compute (owner steer — the asymmetry)

The quantum dilogarithm has a **real (phase / energy)** and an **imaginary (volume)** part.

- **Mass compute — already carries the full octahedron on the *volume* side.** `m(K) = m_e·Vol(K)·ρ`
  uses the **hyperbolic `Vol(K)` = Σ over all ideal tetrahedra** (`Im Φ_q`, the Bloch–Wigner sum).
  So the volume side is octahedrally complete; the separate ~2.89% `m_p` categorical-vs-exact
  `Vol(𝓑₃)` gap is **not** this (though whether the categorical `Vol` under-triangulates is worth a
  check).
- **Binding compute — this is where it bites.** The reeb `μ₀` tier uses the counit **phase**
  `(q−q⁻¹)` = a **single tetrahedron's** first-order term (`Re Φ_q`-side). The **−9% is
  (hypothesis) the other-3-tetrahedra** completion of the *phase* side — the octahedral structure the
  *volume* side already has, missing from the *energy* side.
- **Nothing is wired.** This is diagnostic; it names *what* is missing. Verifying = computing the
  deuteron crossing's octahedral (4-`Φ_q`) holonomy and checking whether the 3-tetrahedra term is
  quantitatively the −9%. **Anti-fit:** it must be computed, never tuned; the §2e entropy bound
  still forbids a factor-scan.

## 4. Solid vs hypothesis (honest)

| | status |
|---|---|
| crossing = octahedron = 4 dilogs = 4 tetrahedra | **solid** (2509.02354 theorem) |
| octahedral state-integral is resurgent (Stokes = tetrahedron faces) | **solid** (GGM; #3805) |
| mass `Vol(K)` sums all tetrahedra; binding `μ₀` uses one | **solid** (structural: volume vs phase side) |
| the deuteron −9% *is* quantitatively the 3-tetrahedra (alien) term | **hypothesis** — to compute, not fit |

## 5. Routes (beans `qou-ch8w`)

- **B (now lead, `qou-3fqa`)** — the octahedral 4-`Φ_q` holonomy; `μ₀` = 1 tetrahedron, resum the
  other 3 (2509.02354). Cross-check against #3805's `A_ω` 3d-index.
- **A (`qou-dp32`)** — Magnus continuation of `F_q = [δq₁,δq₂]`: the log of the 4-`Φ_q` product =
  Σ log `Φᵢ` + commutator/Magnus corrections; `μ₀` is the first-order single term (see the Lean
  `FourDilogFirstOrder.lean` — the 4-factor first-order truncation).
- **C (`qou-xajh`)** — the `(q−q⁻¹)=(v−v⁻¹)·[2]_v` v-level passage.
- **D (`qou-quv8`)** — bar-parity: `μ₀ ∝ (q−q⁻¹)` bar-odd; the octahedron's tetrahedra split
  bar-even/odd.

`E_unit` / the −9% is **not** closed here — this locates the missing structure (the octahedral
completion) and the tool (the 4-`Φ_q` / alien resummation). Anti-laundering stands.

Refs: `library/arxiv-2509.02354v2/2509.02354v2.pdf`, `library/arxiv-math-ph-0012035v3/0012035v3.pdf`, `library/phys-rep09/phys-rep09.pdf` (owner-uploaded,
commit `618466`); #4117 `2026-07-19-eunit-source-is-the-counit.md`; sibling #3805 (`A_ω`);
`climax-volume-mass/crossing-energy-*`.
