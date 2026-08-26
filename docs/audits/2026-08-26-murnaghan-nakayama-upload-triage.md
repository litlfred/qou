# The 2026-08-26 Murnaghan–Nakayama upload drop — ingest + usability triage

**Date:** 2026-08-26 · **Source:** [`548de479`](https://github.com/litlfred/qou/commit/548de479e7026caf77a29f4aa6e1db27e638bef1)
(owner upload, 10 PDFs) · **Beans:** `qou-ximf`, `qou-cds1` ·
**Tier:** ingest + literature triage; **nothing wired, no `c_k` value, no tier moved.**

Owner ask: *"ingest … and see what's usable"* + *"characters on quantum flag
varieties and tetraplectic structure is perhaps a good avenue"*.

## 1. Ingested — all ten, and corpus-grep path 5 now reaches them

`uploads/` is the **incoming queue**; path 5 of the corpus-grep checklist searches
`library/` only, so until this ran the drop was invisible to every "has the corpus
got this?" check. Now `library/` holds 411 documents.

| doc-id | work |
|---|---|
| `9511222v1` | Halverson & Ram, *MN Rules for Characters of Iwahori–Hecke Algebras of G(r,p,n)* |
| `1-s2-0-0097316595900136-main` | Halverson, *A q-Rational MN Rule*, JCTA 71 (1995) 1–18 |
| `arxiv-2504.18825v2` | Jing & Liu, *MN Rule for the Cyclotomic Hecke Algebra and Applications* (v2, 2026-03) |
| `arxiv-2406.05311v1` | Benedetti–Bergeron–Colmenarejo–Saliola–Sottile, *A Quantum MN Rule for the Flag Manifold* |
| `arxiv-2408.04921v2` | Gao & Jing, *Irreducible Characters of the Generalized Symmetric Group* |
| `arxiv-1202.0067v3` | Evseev–Paget–Wildon, *Character Deflations and a Generalization of the MN Rule* |
| `arxiv-1508.01627v4` | Lübeck & Malle, *MN Rule for Unipotent Characters in Classical Groups* |
| `arxiv-1306.3655v1` | Regev, *The MN Rule and Some Virtual Sₙ Characters* |
| `bq28-r2r7` | Bravyi–Gosset–Havlíček–Schatzki, *Classical and Quantum Algorithms for Characters of Sₙ*, PRX Quantum 6 030323 (2025) |

**One duplicate, recorded.** `A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf`
is a second upload of `2406.05311v1.pdf` — same stamp, same 34 pp. Both PDFs sit in
`library/arxiv-2406.05311v1/`; the entry is in
[`library-duplicate-ledger.json`](library-duplicate-ledger.json). **Two grep hits
there are ONE source.**

**Ingest caveat.** `folio-assistant` is not present in this container, so
`pdf-structure.py` could not run; an in-container stand-in produced
`structure.json` + `sections/*.md` + `summary.json` to the same schemas.
**`candidates.json` was deliberately NOT fabricated** — that is the claim
extractor's output. Re-run the real tool to add it. Five titles were hand-corrected
where the extractor picked up a journal masthead ("REPRESENTATION THEORY",
"PRX QUANTUM 6…").

## 2. Usability — one item is directly load-bearing, and one is a trap

### ⭐ Halverson–Ram + Jing–Liu — the general-`n` replacement for hand-derived characters

Both give the MN rule for **Iwahori–Hecke** characters `χ_λ^{H_n(q)}` on
*standard elements*. That is the same object the corpus currently carries **by
hand and only at `n = 3`**: `chi_block_3 / chi_block_21 / chi_block_111` in
`qbeta_utils.py`, and the one-crossing "character collapse"
`2χ_λ(σ₁) − h·f^λ = [2]_q·χ^λ(τ)` derived in the 2026-08-21 ladder-phase audit.

Jing–Liu is the stronger citation and supersedes HR on exactly the point that
matters: HR *"computed characters only on certain standard elements and did not
prove"* completeness; Jing–Liu + Shoji's determinacy give the **full irreducible
character table** of `H_{m,n}(q,u)`, plus a **dual MN rule via vertex operators**.

So the usable thing is a **general-`n` closed form for the per-block Hecke
characters** — the missing ingredient for taking the ladder's per-block structure
beyond `n = 3` without re-deriving it by hand each time.

### 🛑 The flag-manifold paper is a symbol-overloading trap

Its "quantum" is the **quantum-cohomology / Novikov degree parameter** of `QH*(Fl_n)`
— *not* the Hecke deformation `q`. Identifying the two would be exactly the
overloaded-symbol failure the corpus documents repeatedly (registry §2 exists for
this class). The paper's usable content is structural, not parametric: it reduces
quantum products by **hook** Schur polynomials to the classical product via the
quantum Bruhat order (Leung–Li, Postnikov). Cite it for the hook reduction; do not
import its `q`.

### Tetraplectic — already in the library, and not new

`arxiv-math-0104104v3` (*Geometry of Four-vector Fields on Quaternionic Flag
Manifolds*, §3 "Quatrisson and tetraplectic structures") was already ingested. The
owner's avenue is therefore not blocked on acquisition. Not assessed on the merits
here.

## 3. The prune this triage produced — of my own idea

Bean `qou-ximf` proposed the `Ξ_k = (1+Q^k)/(1+Q)^k` family and suggested the
k-cycle Hecke traces as the route to reach `Ξ_{k≥3}`. **Tested exactly at `n = 3`,
convention D, and it fails — scope-(a).**

Building the `H_3(q)` 2-dimensional irrep from the braid + Hecke relations
(verified, `c = 1`) gives `χ_{(2,1)}(σ₁) = h`, `χ_{(2,1)}(σ₁σ₂) = −1`, and against
the D weights:

```
Σ_λ y_λ χ_λ(σ₁)    = z_D          Σ_λ y_λ χ_λ(σ₁σ₂) = z_D²
```

An exact solve for constant rational coefficients returns a one-parameter family
whose `Ξ₃` coefficient is free — i.e. `Ξ₃` **does not enter**. Setting it to zero:

```
4 z_D²  =  h² + ([2]_q Ξ₂)² + 2h·[2]_q Ξ₂  =  (h + [2]_q Ξ₂)²
```

which is the proved `k = 2` identity squared. **Nothing new.** The reason is
structural and kills the whole sub-class: the **Markov property** forces
`tr_M(σ₁⋯σ_{k−1}) = z^{k−1}` identically, so every standard-element Markov trace
is a power of `z` and carries no information beyond `Ξ₂`. The same holds for the
single-crossing powers: `Σ_λ χ_λ(σ₁^k) y_λ` expands over `1` and `Ξ₂` only.

**Consequence, and it sharpens `qou-ximf` rather than killing it.** `Ξ_{k≥3}` is a
**weight functional, not a trace value** — computable from the weight vector, but
not equal to any Markov trace on the ladder's own elements. The Hecke MN rule
therefore does *not* supply a new bridge from the ladder to `Ξ_{k≥3}`; what it
supplies is the general-`n` per-block characters of §2. Anyone reaching for the
k-cycle route should stop here.

**🛑 Superseded the same day — the family itself is withdrawn.** `Ξ_k =
(q^k + q^-k)/[2]_q^k` is a rational function of `[2]_q` alone, and
`[2]_q² = h² + 4`, so every member is a function of `h²` — which the ladder
already carries. So the k-cycle prune below was the *right conclusion for the
wrong reason*: `Ξ₃ = (h²+1)/[2]²` is a redundant coordinate, which is why its
coefficient came out free. `ce` is not hiding in the weights at all. See
[`qbeta_xi_family_collapses_to_h_probe.py`](../../computations/qbeta/qbeta_xi_family_collapses_to_h_probe.py)
(6/6) and the retraction in `qou-ximf`. The anti-fit fence is moot — there is no
family left to fit with.

## 4. Net

Ingest done and greppable. One directly usable item (general-`n` Hecke characters,
Jing–Liu preferred over HR), one flagged trap (the flag-manifold `q`), one avenue
already in hand (tetraplectic), and one honest negative that closes the k-cycle
route into `Ξ_{k≥3}`.
