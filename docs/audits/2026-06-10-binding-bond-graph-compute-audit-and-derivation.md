# Binding bond-graph — compute audit + pre-archimedean per-bond derivation (2026-06-10)

**Status:** compute audit + exploratory derivation (no production rewire yet).
Owner directives: *"fix: the braid wires only A−1 chain bonds; do a full
compute audit"*; *"derive it [f], no |·|"*; *"do everything pre-archimedean
where you can"*; *"use tr_M·\check{tr}_M if needed"*.

Probes (PR #2089):
[`derived_bond_graph_binding.py`](../../computations/derived_bond_graph_binding.py),
[`prearchimedean_bond_factor.py`](../../computations/prearchimedean_bond_factor.py),
[`gs_filtration_binding_components.py`](../../computations/gs_filtration_binding_components.py).

## 1. Compute audit — how the braid wires bonds

`mass_at_3A_proper.atom_braid_word_3A(Z, N)` builds the 3A-strand braid
nucleon-by-nucleon. For each nucleon k (ordering `['p']*Z + ['n']*N`): intra
crossings on σ_{3k}, σ_{3k+1} (the B₃ core), then — **only if `k < A−1`** (line
288) — ONE inter-nucleon bridge `c·σ_{3k+2} + d·1` linking k to k+1:

| pair | (c, d) | source |
|------|--------|--------|
| p-p | (1, 0) | σ (isospin-symmetric) |
| n-n | (1, −h) | σ⁻¹, h = q−q⁻¹ |
| p-n | (1, −h(½−δ/4)) | color-weighted averaged crossing, δ = `_avg_color_delta` |

**The finding (the "bug"):** `k < A−1` wires only the **A−1 CHAIN** bonds
(nucleon k bonds to k+1 only). The `m_pp/m_pn/m_nn` arguments are crossing
*multiplicities* on those chain bonds — **not** an all-pairs lever. Physical
binding involves all `C(A,2)` nucleon pairs; the braid is a path graph, not the
complete graph.

Downstream consumers of `atom_braid_word_3A`: `binding_canonical` (via
`build_atom_symbolic`), `markov_trace_3A` (deprecated Plancherel),
`per_generator_V_hat_3A`, `binding_3A`, `binding_3A_tower`. A change to the
wiring touches all of them — so the fix is **not** to mutate the canonical
braid but to compute the binding over the correct bond graph via the derived
per-bond factor (§3), leaving the chain braid as the existing compute.

## 2. Pre-archimedean derivation of the per-bond factor (f is NOT fitted)

The GS-filtration finding (`gs_filtration_binding_components.py`) measured a
multiplicative per-bond trace suppression `tr_atom ≈ tr_free·f^bonds`, f ≈ 0.39.
That f is now **derived exactly**, and the derivation is **pre-archimedean**
(fibre / formal q):

The free config factors as a product of nucleon traces; each bridge is
GS-independent (far-commutes, |3i−3j|≥3) at a Markov-removable position, so its
contribution to the Jones–Markov trace is the **conditional expectation**
`E_{H_n→H_{n-1}}(c·σ_{n-1}+d) = c·z + d`, where `z(q)=1/(q^{1/2}+q^{-1/2})` is
the Markov parameter (`E(σ)=z`). Hence the trace factorizes over bonds with

| factor | formal-q form | at q₀ | measured |
|--------|---------------|-------|----------|
| `f_pp = z` | `√q/(q+1)` | 0.499320 | 0.499 |
| `f_pn = z − h(½−δ/4)` | `(q^{3/2}−(q+1)(q²−1)/2)/(q(q+1))` (δ→0) | 0.394862 | 0.395 |
| `f_nn = z − h` | `(q^{3/2}−q³−q²+q+1)/(q(q+1))` | 0.290260 | 0.290 |

**Validation:** `∏_{chain} f_bond` reproduces the measured `tr_atom/tr_free`
for D/T/³He/⁴He to **max rel err 1.1×10⁻¹⁵** (machine precision). f is the
Markov factor of the bridge — a Hecke fact in formal q, NOT a fit, NOT
archimedean. The only archimedean step is the single substitution `q → q₀`
(Im q₀ = 0) for the MeV numbers.

**No |·|.** The binding is the pre-archimedean free-energy difference

    B(q) = E_0 · log( tr_free / tr_atom ) = E_0 · Σ_{bonds} log(1/f_bond(q))

which is positive (each `f_bond < 1`), so no modulus is needed. `E_0 =
m_e/(q₀(q₀−1)) ≈ 4.186 MeV` is the deuteron-fixing canonical scale (not Q_β).

Derived per-bond energies (substrate-fixed): **pp = 2.907, pn = 3.890,
nn = 5.178 MeV**.

### Bar product (used where a norm is wanted)
If a norm is needed (complex fibre traces), the archimedean realization is the
**bar product** `tr_M·\check{tr}_M` (q→q⁻¹), NOT `|·|`. Under the bar
involution `z→z` (bar-symmetric) and `h→−h`, so `f_pp·\check{f_pp}=z²`,
`f_nn·\check{f_nn}=z²−h²`, `f_pn·\check{f_pn}=z²−h²(½−δ/4)²`. The bar-norm
per-bond energies `(E_0/2)·log(1/(f·\check f))` are **more uniform**
(pp 2.91, pn ≈ 3.0, nn ≈ 3.3 MeV) — recorded in
`derived-bond-graph-binding.witness.json` as the `*_bar` columns. At q₀ the
plain log-ratio (real traces) is the natural fibre object; the bar variant is
kept for the norm-needing case.

## 3. The fix — binding over the bond graph

With the derived `f_bond`, the binding over any bond graph is a closed sum:

| graph | edges | D | T | ³He | ⁴He | miss range |
|-------|-------|---|---|-----|-----|-----------|
| **chain** (as-wired) | A−1 | 3.89 | 9.07 | 6.80 | 11.98 | 0.57–2.36× |
| **complete** (all-pairs) | C(Z,2) pp + Z·N pn + C(N,2) nn | 3.89 | 12.96 | 10.69 | 23.64 | 0.57–1.20× |
| B_AME | | 2.225 | 8.482 | 7.718 | 28.296 | — |

(linear `B=Q_β·Δtr` baseline missed 4.8–39.7×.)

**Reading:** f is derived; the per-bond *energies* are fixed substrate
quantities; only the **edge set** is open. The chain under-binds (⁴He 2.36×);
the complete graph over-binds the light nuclei (D 0.57× = 1.75× over) and lands
⁴He at 1.20×. The physical bond graph is between chain and complete —
saturation / Pauli blocking / shell structure (the deuteron is anomalously
loose; ⁴He is doubly-magic). That edge-set selection is the remaining
structural question — NOT a fitted Δ_λ closure (the per-bond physics is fixed;
no 7th ansatz).

## 4. Pre-archimedean / Z_q heat-flow connection (peaceful-brown)

`tr_M = Σ_λ y_λ(q)·χ_λ(q)` is a **Wedderburn heat trace** — the Z_q partition
function of `claude/peaceful-brown-hrt19q` §3-bis (pre-archimedean depth-1 heat
backbone: `exp_q` shift kernel `R(q,x)=1+(q−1)x`, per-mode
`R_λ(q,t)=1−(q−1)μ_λ(q)t`, Z_q assembly). The inter-nucleon bridge is the
**depth-1 link kernel** on the Wedderburn eigenbasis; linking a bond multiplies
Z_q by the mode-averaged factor `f_bond`, so the bond-graph binding is the
**free energy of the q-heat flow**, `B = E_0·log(Z_free/Z_atom)`. This is the
pre-archimedean home of the binding; the Lean module
`QBetaPreArchHeatDepthOneKernel.lean` on that branch formalizes the kernel
(generic CommRing — fibre level), the natural place to also state
`f_bond = c·z + d`.

## 5. Status / next

- ✅ Compute audit (chain A−1 wiring); ✅ f derived exactly (pre-archimedean);
  ✅ bond-graph binding (chain vs complete); ✅ bar variant; ✅ Z_q link.
- Open: the **edge-set selection** (chain/complete/shell) — the physical bond
  graph. Likely the saturation/Pauli structure, possibly the same shell physics
  as the per-nucleus volume route (#2078).
- Lossless χ extended to ⁵Li/⁶Li (Rust path) for the A=5,6 active sets.

## 6. Update (same day) — edge-set selection REFUTED by exact enumeration

[`bond_edge_set_selection_probe.py`](../../computations/bond_edge_set_selection_probe.py)
enumerates **every** static integer edge multiset per nucleus (the full class
`0 ≤ n_pp ≤ C(Z,2)`, `0 ≤ n_pn ≤ Z·N`, `0 ≤ n_nn ≤ C(N,2)`) against the
derived per-bond energies. **No static bond graph closes D/T/³He/⁴He
jointly:**

| nucleus | best integer set | miss | closable ±5% |
|---------|-----------------|------|--------------|
| D | (0,1,0) — its only bond | 0.57× | ✗ (needs occupancy ≈ 0.57 — halo) |
| T | (0,1,1) = chain | 0.94× | ✗ (close) |
| ³He | (0,2,0) | 0.99× | ✓ alone |
| ⁴He | (1,4,1) = complete | 1.20× | ✗ (needs **more** than all pairs — magic) |

The two joint blockers are exactly nature's two famous anomalies (halo
deuteron, doubly-magic α). Verdict: the bond graph is **not a static integer
graph** — the remaining structure is **fractional bond occupancy / shell
weighting** (saturation, Pauli, magic), i.e. the per-nucleus volume route
(#2078). Formalize-first refutation recorded so the static-graph direction is
not re-chased.

## 7. Lean formalization (fibre-level, sorry-free)

[`QOU/Hecke/MarkovBondFactor.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/MarkovBondFactor.lean):
`trace_bond_crossing` (`tr_M(c•σ_i + d•1) = c·z + d` — the per-bond factor)
and `trace_bond_pair_factorizes` (`tr_M((c₁σ_i+d₁)(c₂σ_j+d₂)) =
(c₁z+d₁)(c₂z+d₂)`, i<j — the two-bond factorization), both proved from the
existing `MarkovTrace` class fields (generic `CommRing R`, no archimedean
structure — per CLAUDE.md §7c). The general A-bond product needs the
cross-level Markov axiom the class does not yet carry (same gap as
`markov_trace_unique`); the compute witness covers it numerically to 1.1e-15.
