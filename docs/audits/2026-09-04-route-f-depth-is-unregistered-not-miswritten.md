# Route F: "depth" is UNREGISTERED, not miswritten — and there are at least five senses, not three

**Date:** 2026-09-04
**Beans:** `qou-zovy` (route F, the action), `qou-hnri` (the measurement side),
`qou-wjbd`, epic `qou-2q85`

## 0. What route F was going to do, and why that is the wrong edit

`qou-zovy` states the fix as:

> name them distinctly in `notation/notation-register-table3-data.md` and
> `notation-collisions.md` — transcendence depth `n`, cell `λ_K`,
> curvature-rank `k` — and stop using the bare word "depth" for (3).

Measured before editing. **`notation-register-table3-data.md` has no depth
row**, and neither does any other register table. The word "depth" occurs
exactly three times in the whole notation register, all incidentally:

| file | occurrence | what it is |
|---|---|---|
| `notation-collisions.md:118` | `B_depth = Σ_k α_k Φ_k` | a row about a *tower*, in a table about `B` |
| `notation-register-table4-data.md:4` | a cross-reference to `conj:gb-depth-period-correspondence` | a label, not a definition |
| `notation-register-table7-data.md:5` | "truncations `𝔈_0^{(N)}` for depth `N`" | the brane-tower index, inside the *energy* row |

So there is nothing in table 3 to rename, and the collision is not a defect in
the register — **it is an absence from it.** The register never registers
"depth" at all, which is precisely why the name was available to be taken
repeatedly without anything flagging the reuse. The correct edit is an
*addition* (a collision entry enumerating the senses), not a rename.

## 1. The bean says three senses. At least five are distinct.

Measured across `content/quantum-observable-universe/**/*.md`: `the depth` 151,
`at depth` 65, `depth-period` 56, `iterated-integral depth` 20, and a tail of
qualified forms. Sampling each qualified form:

| sense | the object | in the bean? |
|---|---|---|
| **transcendence / iterated-integral** `n` | `G^(n)` adjoins `Li_n^q`; `τ_arch(G^(n)) ⊆ 𝒫_n`; moved additively by the q-shuffle | yes (1) |
| **knot / Hecke cell** `λ_K ⊢ n_K` | the partition cell of the atom's braid | yes (2) |
| **GB / curvature-rank** `k = depth(λ) − 1` | partition depth (max hook length) | yes (3) |
| **cascade depth** `N_eff = ⌊log_q(Re_q^{3/4})⌋` | the q-turbulence Reynolds cascade (Ch 7) — a fluid-dynamics cutoff, not a filtration at all | **no** |
| **brane-tower / truncation depth** `N` | `𝔈_0^{(N)}`; `conj:n-v-tower-depth-ninety` ("depth from `m_e` to `v` equals 90"); `N_v = 120·q_0^90` | **no** — and this is the one sense the register *does* already carry |

Two further names are identified with senses above **by propositions**, so they
are one thing or two depending on those propositions' status:

- **NF support depth** — `prop:phi-q-categorical-truncation` asserts
  *"brane-tower truncation depth = NF support depth"*. Same object only if that
  proposition holds.
- **slicing depth** — `mass-theory/atom-knot-mass-derivation-table1-data.md`
  gives the row `slicing depth | GB filtration grade ℓ(w) (Coxeter length)`,
  and the proof text uses *"finite slicing depth = filtration grade ≤ k"*.

Two more, **not** counted as new senses: **cyclotomic depth** and
**Bring-natural depth**. Both appear to be the transcendence sense under a
different adjective — `Cl_3(2π/5)` as a "Bring-natural depth-3 invariant",
`β(3) = π³/32` from "cyclotomic depth-`n` generators", where depth 3 pairs with
the trilogarithm exactly as sense (1) requires. Recorded as *probably
synonymous*, not measured to be.

So: the bean's three is an undercount by at least two, and the sense already in
the register is not among its three.

## 2. A claim I nearly wrote, and did not — recorded because the near-miss is the point

Having found `slicing depth = ℓ(w)` in the mass derivation's own dictionary, the
tempting write-up was:

> the atom-knot mass derivation identifies its slicing depth with a filtration
> reading the corpus has refuted (`qou-wjbd`, the Coxeter-length reading).

**That is false, and it is the exact error class this PR proves a theorem
about.** `qou-wjbd` does not refute the Coxeter-length filtration. What it
refutes is the **bridge** — the identification

    Z^(k) = Z ∩ F_k   ↔   {λ ⊢ n : gbDepth(λ) = k}

between the *centre's* graded strata and the *partition* strata, measured
exactly over three backends and failing at every `n`, with a filtration-agnostic
degree-0 obstruction on top. The Coxeter-length grading `ℓ(w)` on `H_n(q)` is
untouched by that and remains a perfectly good filtration; the mass derivation's
row defines a grading and asserts no bridge.

Inferring the second from the first is reading a property of one construction
*built on* an object as a property of the object — the same shape as
`AmbientInvolutionDoesNotDecideType` (an ambient group's outer automorphism read
as one representation's Frobenius–Schur type), committed to this branch hours
earlier. It survived a topic-grep and was caught only by reading `qou-wjbd`'s
own statement of what it excluded.

## 3. What route F should therefore do — and what needs the owner

**Not blocked, done here:** this measurement, and the correction to `qou-zovy`'s
plan.

**Needs the owner**, because it is a content edit to the paper's authoritative
notation register with corpus-wide reach, and because two of the seven names are
one-or-two depending on a proposition's status:

1. Whether to add a **`depth` collision entry** to `notation-collisions.md`
   enumerating the senses with distinct symbols — an addition, not the rename
   the bean proposed.
2. Whether **NF support depth** and **slicing depth** get their own rows or are
   folded into the senses their propositions identify them with.

**The bean's own warning still stands and is strengthened by this.** It says a
reader who fixes only the names will still think there is a filtration behind
the curvature-rank sense, when all three readings of `J^•` are excluded. The
measurement here adds that a reader who fixes the *three named* senses will
still meet a cascade cutoff and a brane-tower index under the same word.
