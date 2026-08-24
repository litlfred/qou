# Obstruction A, measured: the corpus's own meson braid has Vol = 0 (2026-08-24)

**Bean:** `qou-qpj9` · **Tool:** SnapPy 3.3.2 · **Status:** measurement + prune, **no braid proposed, no mass fitted**

## What was measured

`def:categorical-meson` fixes the meson braid explicitly:

$$\mathfrak{M} = T_{01}\cdot\mathcal{L}_H\cdot T_{10} = (\sigma_0\sigma_1)^2\cdot\sigma_1\sigma_0$$

— 6 crossings on 3 strands. Nobody appears to have closed it and computed the volume. Doing so:

| object | braid | comps | Vol | solution type |
|---|---|---|---|---|
| **meson `𝔐`** | `(σ₀σ₁)²σ₁σ₀` | 1 | **0** | contains flat tetrahedra |
| `L₊` Hopf | `σ₀σ₁` | 1 | 0 | degenerate |
| `(σ₀σ₁)³` full twist | — | 3 | 0 | degenerate |
| trefoil | `σ₀³` | 1 | 0 | flat |
| Borromean | `(σ₀σ₁⁻¹)³` | 3 | 7.32772475342 | positively oriented |

The Borromean row is the control: it reproduces `2·V_oct` to 11 places, so the pipeline is sound.

**Identification via the knot group** (`determinant`, `signature` and `alexander_polynomial` all require Sage, which is absent; the fundamental group does not):

| braid | relator | group | knot |
|---|---|---|---|
| `(σ₀σ₁)²σ₁σ₀` | `aabbbbb` | `⟨a,b ∣ a²=b⁵⟩` | **T(2,5) = 5₁** |
| `σ₀⁵` | `aaaaabb` | `⟨a,b ∣ a⁵=b²⟩` | T(2,5) ✓ |
| `σ₀³` | `aabbb` | `⟨a,b ∣ a²=b³⟩` | T(2,3) ✓ |

The meson braid closes to the **cinquefoil** — the knot the corpus assigns to the **muon** — and it simplifies from 6 crossings to 5.

## Consequence

Under the volume–density mass law `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`, the corpus's own pion braid gives **m_π = 0**. Obstruction A is therefore not a gap in a search that has not been run; it is a property of the construction already written down.

**Diagnosis.** `lepton-meson-parallel` says "the binding Hopf link introduces negative crossings via `σ⁻¹ = σ − h`". That is true in the **Hecke algebra** — `L₋` appears in the normal form with coefficient `h` — but the **braid word is entirely positive**. Negative crossings in a normal-form *coefficient* are algebra, not geometry, and volume sees only the geometry. The construction conflates the two.

## Target volumes (what any candidate must hit)

`ℏ_q² = 0.00981718645427507381` at the proton pin; `Vol·ρ = (m/m_e)·ℏ_q²`.

| meson | m [MeV] | m/m_e | **Vol·ρ needed** |
|---|---|---|---|
| π± | 139.57039 | 273.132 | **2.681392089** |
| K± | 493.677 | 966.102 | **9.484401401** |
| K⁰ | 497.611 | 973.800 | 9.559980444 |
| η | 547.862 | 1072.139 | 10.52539033 |
| D⁰ | 1864.84 | 3649.401 | **35.82684854** |
| J/ψ | 3096.900 | 6060.482 | **59.49688298** |
| η_c | 2983.9 | 5839.347 | 57.3259547 |
| *(μ, for scale)* | 105.658 | 206.768 | 2.029882787 = Vol(4₁) |

## The prune — and a correction to my own first attempt

**First attempt, WRONG.** From a deduplicated enumeration I concluded "no positive 3-braid closure is hyperbolic, so the construction must admit `σ⁻¹`". Tested directly: of **2044** positive words on `{σ₀,σ₁}` of length 2–10, **208 have hyperbolic closures**. The claim is false; the sample was deduplicated by volume and length-limited, which under-represented positive words. Recorded because it is the shape of error this corpus keeps punishing — an inference from a filtered sample, presented as structural.

**What survives, and it is sharper.** The measured minimum hyperbolic volume over positive 3-braids (length ≤ 10) is **4.851171**. The pion needs **2.681**. So *at ρ = 1* the pion's target lies **below the entire positive-braid hyperbolic spectrum**, while mixed-sign words reach 2.0299 (`4₁`, at `(σ₀σ₁⁻¹)²`) and 2.8281 (`5₂`). This is a **conditional** prune — `ρ` is the per-block density and is not 1 in general — so it constrains `(braid, ρ)` jointly, not the braid alone.

Smallest hyperbolic volumes found, 3-braid words length 3–8 (30 distinct volumes):

| Vol | comps | word |
|---|---|---|
| 2.029883213 | 1 | `[1,-2,1,-2]` (4₁) |
| 2.828122088 | 1 | `[1,1,1,2,-1,2]` (5₂) |
| 3.663862377 | 2 | `[1,1,-2,1,-2]` (Whitehead) |
| 4.059766426 | 2 | `[1,1,1,1,2,-1,2]` |
| 4.124903252 | 1 | `[1,1,1,2,-1,-1,-1,2]` |
| 7.327724753 | 3 | `[1,-2,1,-2,1,-2]` (Borromean) |

## What this does NOT do

No braid is proposed for any meson, and **no mass check was run**. The nearest enumerated volume to the pion target is `5₂` at 5.47 % — that is *not* a result, it is the distance to the nearest point of a dense set, and selecting on it would be the per-state fit the J/ψ attack already recorded as worthless. The J/ψ and D⁰ targets (59.50, 35.83) lie far above anything reachable at these braid lengths, so the candidate space is not even bounded yet at the heavy end.

## Literature

The corpus library (332 documents) carries the volume-conjecture line — Kashaev's quantum-dilogarithm volume (`arxiv-q-alg-9601025v2`), the VC introductions (`arxiv-1002.0126v1`, `arxiv-1003.4808v2`), refined/categorified VC (`arxiv-1203.2182v1`) — but **nothing on the classification or volumes of closed 3-braids**, which is exactly the tool Obstruction A needs.

Externally the relevant results are:

- **Murasugi's classification of 3-braids** up to conjugacy, and **Birman–Menasco**'s solution of the link-type classification for closed 3-braids: a closed-3-braid link type is a single conjugacy class, except for braid index 1–2 and one unexpected infinite family of invertible links with two 3-braid axes. ([Birman–Menasco, *A note on closed 3-braids*](https://arxiv.org/pdf/0802.1072); [*Studying links via closed braids III*](https://msp.org/pjm/1993/161-1/pjm-v161-n1-p02-p.pdf))
- **Murasugi/Schreier normal form**: every 3-braid is conjugate to `Δ^{2ℓ}a^p`, `Δ^{2ℓ+1}`, `Δ^{2ℓ}ab`, `Δ^{2ℓ}(ab)²`, or `Δ^{2ℓ}a^{-p₁}b^{q₁}⋯a^{-p_r}b^{q_r}`. Hyperbolicity is characterised in terms of this form, and **volume bounds for hyperbolic closed 3-braids are expressed in its parameters** — the `r`-syllable count. ([Futer–Kalfagianni–Purcell line: *Cusp areas of Farey manifolds*](https://arxiv.org/pdf/0808.2716); [*Semi-adequate closed braids and volume*](https://arxiv.org/pdf/1406.7337))
- Structural properties of closed 3-braids: nearly fibred, unique incompressible surface. ([*Properties of closed 3-braids*](https://arxiv.org/pdf/math/0606435); [*Closed 3-braids are nearly fibred*](https://arxiv.org/pdf/math/0510243))

**These are search-result summaries, not read papers** — I did not fetch the FKP theorem statements, so the exact volume-bound constants are not quoted here and must be checked before use. `search_arxiv` returned empty for every query including "knot theory", i.e. the tool is not reaching arXiv; this came from web search instead.

**Why the normal form is the right next tool.** It replaces "search the braid space" with "solve for the syllable parameters `(ℓ, p_i, q_i)` that a target volume admits". That is a formalize-first prune of exactly the sanctioned kind — narrow the class first, then check once — rather than a scan that lands on `m_D`.

## Open question for the author

Whether the meson braid must be a **knot** (1 component) or may be a **link**. The corpus's `𝔐` closes to a knot, but `q̄q` is a two-constituent state, and the two-component hyperbolic candidates (Whitehead 3.664, and 2-component words at 4.060, 4.749, 6.138) are otherwise inaccessible. This changes the candidate space before any search, so it wants deciding first.
