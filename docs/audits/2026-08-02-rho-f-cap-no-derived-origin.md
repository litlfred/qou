# ρ_F cap at 2 has no derived categorical origin — and ⁴He isn't an integer (2026-08-02)

Branch `claude/q-deformed-saddle-offsets-bdn992` (PR #4598). Resolves bean qou-58r5
(option B). Follows `2026-08-02-he4-nu-sdp-decisive-2-not-3.md` (⁴He ρ_F ≈ 2, not 3).

## Question

After ⁴He killed the monotone {sc(3A)=A−1} family, the surviving data is
ρ_F = {²H:1, ³H:2, ³He:2, ⁴He:~2}, fit by `min(A−1, 2)`. Is the **cap at 2** (the
regime switch A−1 → ~2) a *derived* categorical count, or numerology?

## Answer: NO derived origin. The cap is empirical, and ⁴He isn't even an integer.

**The reframing that undercuts the premise.** ⁴He's value is not the integer 2 — it is
the data-pinned `ρ_F(⁴He) = B_AME/(m_e·A·8G) = 1.889` that the corpus rounds. The two
cleanest categorical counts **bracket** it and neither lands:

| candidate | ²H | ³H | ³He | ⁴He | verdict |
|-----------|----|----|-----|-----|---------|
| data | 1 | 2 | 2 | **1.889** | — |
| isospin `2T+1` | 1 | 2 | 2 | **1** (T=0) | fails ⁴He *low* |
| monotone `A−1` = `sc(3A)` | 1 | 2 | 2 | **3** | fails ⁴He *high* (already refuted) |
| `min(A−1, 2)` | 1 | 2 | 2 | 2 | a fit (reverse-engineered) |

⁴He = 1.889 sits **strictly between** the isospin count (1) and the monotone count (3)
— verified this session. A quantity no clean integer count reproduces, whose "value" is
a rounded non-integer, is the signature of an **empirical prefactor**, not a categorical
multiplicity. **This breaks the `ν_SDP ∈ ℤ_{>0}` identification of
`conj:kashaev-density-equals-sdp-multiplicity` at exactly A=4.**

## Candidates tested (adversarial), all fail to DERIVE the cap

1. **Isospin.** `dim(fundamental)=2` is constant (predicts {2,2,2,2}, deuteron wrong).
   `2T+1` gives {1,2,2,**1**} — fails ⁴He *low* (T=0), coincides on D/T/³He only because
   `2T+1 = A−1` there by accident.
2. **Bar-parity classes (bar-even/bar-odd = 2).** A genuine derived ceiling of 2, but
   *constant* (can't give deuteron=1); and the deuteron activates *both* sectors, so
   "#active sectors" = 2 even for D. Suggestive ceiling, derives nothing about ρ_F.
3. **⁴He interface-operator exchange spectrum {±√5,±1} → 2 distinct magnitudes.** The
   striking near-miss. Building the signed [1^A] exchange matrix S (pp=+, nn=−, pn=+)
   and counting #distinct |λ| gives {²H:1, ³H:2, ³He:2, ⁴He:2} — an *exact* match.
   But it fails every adversarial test (verified):
   - **Does not cap at 2:** A=5 (pppnn) → spectrum {−2.37,−1,−1,1,3.37}, 3 distinct
     magnitudes. No structural ceiling.
   - **Selected functional:** only #distinct |λ| matches; #distinct-eigenvalues={2,2,2,4},
     #positive={1,2,1,2}, rank={2,3,3,4} all fail. Picking the one functional that yields
     {1,2,2,2} is a form-fit.
   - **No link to ν_SDP:** S is a 4-body cumulant on A nucleons, not the Wedderburn
     multiplicity of the SDP-saturating projection in H_{3A}(q). Equating them needs a
     proof; none exists.
4. **#closed shells.** {0,1,1,2} — off by one everywhere; fixes are ad hoc.
5. **Wedderburn/partition count capping at 2.** Any partition count of H_{3A} grows with
   A; the concrete instance sc(3A) is already refuted (predicts ⁴He=3).

## The one genuinely derived fact nearby (bounds domain, not value)

SU(4) He4-locality: `rank Λ^A(ℂ⁴) = C(4,A) = 0` for A>4 (Lean-proved,
`SU4SupermultipletGate.lean`) — ⁴He is the unique doubly-magic fully-antisymmetric
singlet, so the ≥4-body term is ⁴He-local. This explains *why ⁴He is special* (the
domain cap A≤4), **not** why its prefactor is ~2.

## Verdict (scope-(a)) + re-scope recommendation

- **The ρ_F cap at 2 has no derived categorical origin** (none of the tested candidates
  forces it; the matching one — exchange-magnitude count — is a non-capping selected
  functional unrelated to ν_SDP).
- **Deeper:** ⁴He ρ_F = 1.889 is a data-pinned effective prefactor, not an integer
  Wedderburn multiplicity. `min(A−1,2)` is numerology (reverse-engineered).
- **Recommendation:** scope `conj:kashaev-density-equals-sdp-multiplicity` (ρ_F = ν_SDP
  ∈ ℤ) to **census-knot / linear-chain atoms** (²H,³H,³He), where ρ_F = A−1 is exact and
  the SDP framing is canonical. At the doubly-magic point the prefactor is empirical
  (~1.89, Coulomb-corrected ~1.94) and should be treated as an *effective binding
  coefficient*, not claimed as an integer categorical count. The honest open successors:
  (a) is ρ_F even integer-valued at doubly-magic nuclei? (b) derive the doubly-magic
  prefactor directly, including Coulomb, rather than rounding 1.89 → 2.

This is scope-(a) (no derived origin *found*, value is non-integer at ⁴He), not scope-(b)
(no proof that no categorical object could ever exist). Nothing wired; no closure.
