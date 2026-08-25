---
# ptlm
title: 'Read the uploaded Ptolemy papers: verify the novelty assessment, and price the Ptolemy route past the Gröbner ceiling'
status: completed
type: task
priority: high
tags:
    - literature
    - hyperbolic-volume
    - gluing-equations
    - ptolemy
parent: m015
created_at: 2026-08-10T01:35:00Z
updated_at: 2026-08-10T06:00:00Z
---

Two primary sources were uploaded to the repo at
[`765457e`](https://github.com/litlfred/qou/commit/765457e64bf8b1e862decd2e91171c8a7df1e605):

- `library/arxiv-1207.6711v1/1207.6711v1.pdf` — Garoufalidis–Goerner–Zickert, *Gluing equations for
  PGL(n,ℂ)-representations of 3-manifolds*
- `library/arxiv-1507.03238v3/1507.03238v3.pdf` — *Triangulation independent Ptolemy varieties*

⚠ **They are on `main`, not on the Route 75 branch** — fetch before reading.

## Why this matters — two open questions Route 75 left on a search snippet

**1. The novelty assessment rests on a search result, not on the papers.** Route 75's
docstring and bean `m015` both state flatly that none of the mathematics is new, citing
these two papers plus Thurston, Neumann–Zagier, Neumann–Reid and `snap`. That assessment
is almost certainly right, but it was made from a search summary. **Read the sources and
either confirm it or correct it.** Getting this wrong in the conservative direction costs
nothing; getting it wrong in the other direction would be a false novelty claim in the
corpus.

Specifically, confirm the sentence Route 75's gate G7 leans on — that Gröbner
computations are *"usually impractical for the gluing equations even when the cusp
equations are added"* — is actually in 1207.6711 and says what G7 claims it says.

**2. The Ptolemy variety may be the way past the measured ceiling.** The same snippet
says Gröbner bases **are** feasible for *Ptolemy* varieties "even for many simplices",
while being impractical for gluing equations — and that a **monomial map** recovers the
shapes from Ptolemy coordinates. If that holds, it directly attacks what Route 75
measured:

| Route 75's ceiling | what Ptolemy might give |
|---|---|
| Gröbner derivation dies at 4 tetrahedra (gate G7) | Gröbner reportedly fine "for many simplices" |
| identification (LLL) fails for 11a1/11a2/12a1 (17–20 tets) | exact solutions with **no LLL at all**, hence no height/precision gate and no identification step |

That would make the whole pipeline float-free end to end, at every size — not just up to
3 tetrahedra. It would also retire gate G2's LLL-artifact trap by removing LLL.

## What to produce

1. A verdict on the novelty assessment: confirmed, or corrected in `m015` + the probe
   docstring.
2. A priced plan for the Ptolemy route, with the monomial map written down explicitly,
   and a decision on whether SnapPy's bundled `ptolemy` module can run **without** Sage
   or Magma in this environment — that is the practical blocker, since `find_field`
   already needs Sage (which is why Route 75 re-implements identification by hand).
3. If it runs: extend Route 75, or open a Route 76.

## Related

- `m015` — the gluing-data lane; Route 75's measured ceiling is recorded there.
- `glnl` — Lean-proving the equations; unaffected by which method produced the shapes.

---
**2026-08-10 — both papers read. Novelty assessment CONFIRMED against the primary
sources; Ptolemy route priced and BLOCKED in this container.**

### 1. The quote is real, and G7's citation is correct

Verbatim from **1207.6711 §1.3** (Garoufalidis–Goerner–Zickert):

> *"For the Ptolemy varieties exact computations are possible for n = 2 even when there
> are many simplices, and there are often several components of representations besides
> the geometric one. We should point out that while Gröbner basis computations are
> feasible for the Ptolemy varieties even for many simplices, **they are usually
> impractical for the gluing equations even when the cusp equations are added.** However,
> the monomial map µ can be used to obtain shapes from Ptolemy coordinates. All our tools
> will be available in the upcoming release of SnapPy."*

So Route 75's gate G7 cites this correctly and **the novelty assessment stands as
written**: G7 rediscovers a documented fact. No correction needed to the probe docstring,
bean `m015`, or the PR. Extra detail worth carrying: *"often several components besides
the geometric one"* — which is precisely why Route 75 needs its Bloch–Wigner volume
cross-check to pin the geometric root.

### ⚠ A near-miss worth recording as a method lesson

My first pass grepped both PDFs for `[Gg]r[oö]bner` and got **zero hits in both**, and I
was one step from recording "the citation is misattributed". The extractor renders the
umlaut as `Gr¨ obner` — diacritic split off, with a space inserted — so the pattern could
not match.

> **A zero-hit grep over PDF-extracted text is not evidence of absence.** Ligatures,
> diacritics and hyphenation routinely break naive patterns. Search for a
> diacritic-free substring (`impractical`, `bner`) before concluding a source does not
> say something.

Same family as the standing rule that negative claims cannot come from a grid. It would
have produced a confident, wrong correction to a citation that was right.

### 2. The Ptolemy route: real, and NOT runnable here

Both papers use **Magma** for the primary decomposition — 1207.6711 §14 computes the
decomposition of the gluing+Ptolemy ideal with it, and 1507.03238's Algorithm (Step 3)
is "compute the primary decomposition of the reduced Ptolemy variety `P(T,E)red`".

Tested directly. `snappy.Manifold("4_1").ptolemy_variety(2, obstruction_class=0)` builds
fine, then **both** solution paths fail:

- `retrieve_solutions()` → `RuntimeError: Problem connecting to server … <urlopen error
  Tunnel connection failed: 403 Forbidden>` for
  `https://ptolemy.unhyperbolic.org/data/pgl2/LinkExteriors/02_tetrahedra/4_1__sl2_c0.magma_out.gz`
  — the precomputed database is **network-blocked by the agent proxy**.
- `compute_solutions()` → `ValueError: Sorry, could not find the Magma executable`.

So the answer to this bean's practical question is **no**: the Ptolemy route cannot clear
Route 75's ceilings in this environment. It is blocked on infrastructure, not on
mathematics.

**To unblock, one of:**
1. allowlist `ptolemy.unhyperbolic.org` in the environment's network policy — cheapest by
   far, since the database is precomputed and covers the census;
2. install Magma (licensed) or run SnapPy inside Sage, which would also give
   `tetrahedra_field_gens().find_field()` and retire Route 75's hand-rolled LLL
   identification along with gate G2's artifact trap;
3. implement primary decomposition over ℚ locally — a much larger job, and not obviously
   worth it given (1).

**Recommendation: (1).** It is a one-line policy change and would let the Ptolemy route be
evaluated properly. Until then Route 75's gated-LLL pipeline remains the only working
path, and its measured ceiling (identification, not verification) stands.

---
**2026-08-10 (later) — UNBLOCKED. The route runs locally with Singular. Magma was never
required, and cannot be obtained anyway.**

The previous entry recommended allowlisting `ptolemy.unhyperbolic.org`. Retested: still
403, and the proxy's own `recentRelayFailures` records it as
`connect_rejected … policy denial` for `ptolemy.unhyperbolic.org:443`. **That
recommendation is now superseded — the network is not needed either.**

### Magma cannot be cloned, and is not the point

Magma is **proprietary, commercially licensed** software from the University of Sydney's
Computational Algebra Group. It is not open source, is not on GitHub, and there is no
legitimate way to obtain it by cloning. So "clone Magma" has no answer.

But it is also **not necessary**. The step both papers use Magma for is *primary
decomposition of a polynomial ideal*, and that is exactly what **Singular**'s `minAssGTZ`
does — Singular being the engine **Sage itself calls** for `primary_decomposition()`.
It is free, packaged, and installs in one command:

    apt-get install singular          # 4.3.2, already in the archive

### The route works, verified against results the corpus already proved

`computations/probes/qbeta_route76_ptolemy_singular_probe.py`, 4 gates, all passing.
SnapPy yields the Ptolemy equations **offline** (`equations_with_non_zero_condition`);
Singular decomposes them.

| knot | Singular result | matches |
|---|---|---|
| 4₁ | `c² − c + 1` | the shape field `x²−x+1`, `FigureEightTriangulation.w_sq_sub` |
| 5₂ | `c³ − c² + 1` | **`fiveTwoShapeCubic`** — the corpus's own Landen image of the saddle cubic `y³−2y²+3y−1`, related by `landen_root` |

That 5₂ agreement is the strongest calibration available: the Ptolemy route lands on the
*shape* cubic the corpus already derived by a completely different path (Landen
substitution from the saddle cubic), with `landen_root` already proved in Lean.

**Fully symbolic end to end.** No LLL, no height cap, no precision-stability gate — so
Route 75 gate G2's lattice-artifact risk **does not arise here at all**. This is the
float-free derivation Route 75's G7 could only reach up to 3 tetrahedra.

### ⚠ The obstruction class is not optional

For **both** 4₁ and 5₂ the class-**0** Ptolemy variety is **empty** — Singular returns
the unit ideal, `dim = −1` — and the geometric representation lives on class **1**. A
probe defaulting to `obstruction_class=0` would conclude these manifolds have no
boundary-unipotent representations at all, and it would look like the *method* failing
rather than a mis-set flag. Pinned as gate G2.

(Noticed by hand first: with `c_0011_0 = 1`, class 0's two relations give `c²+c−1 = 0`
and `c²−c−1 = 0`, forcing `c = 0` and then `−1 = 0`. The Singular `dim = −1` confirmed it.)

### ⚠ NOT YET MEASURED: whether it beats Route 75's ceiling

GGZ claim Gröbner is feasible for Ptolemy varieties "even for many simplices". **This is
not yet confirmed here.** A scaling run over 6₁, 7₂, 10_100 and 11a1 produced **no output
after ~15 minutes** — 6₁ alone had not finished. That is *not* evidence of a ceiling
(the run may simply be slow, and `minAssGTZ` has known bad cases), and it must not be
recorded as one.

**Next:** re-run the scaling test with per-manifold timeouts and record what completes,
including the negative results. Also try `primdecGTZ` vs `minAssGTZ`, and a `degrevlex`
ring, before drawing any conclusion about reach. Until then the only verified claim is
that the route **runs**, on 4₁ and 5₂, without Magma or network.

---
**2026-08-10 (later still) — reach MEASURED. It does not beat Route 75, and that
corrects the expectation this bean itself set.**

The previous entry left reach unmeasured and said so. The scaling run has now finished.

### Two independent routes, same fields (gate G5)

| knot | Ptolemy minpoly (Singular) | Route 75 shape minpoly (LLL) | disc | same field? |
|---|---|---|---|---|
| 4₁ | `x² − x + 1` | `x² − x + 1` | −3 | yes |
| 5₂ | `x³ − x² + 1` | `x³ − 2x² + 3x − 1` | −23 | yes |
| 6₁ | `x⁴ − x³ + x² + 1` | `x⁴ − 3x³ + 6x² − 5x + 2` | 257 | yes |
| 7₂ | `x⁵ − x⁴ − x³ + x − 1` | `x⁵ − 2x⁴ + x³ + 3x² − 5x + 3` | 4409 | yes |

`nfisisom` says isomorphic in all four cases, discriminants match. The routes **share no
step** and return **different minimal polynomials**, so this is a real cross-check, not a
tautology — symbolic ideal decomposition and LLL-from-numerics independently land on the
same number fields.

### ⚠ The reach result, which is the opposite of what I implied (gate G6)

| manifold | tets | Ptolemy + Singular | Route 75 LLL + PARI |
|---|---|---|---|
| 4₁, 5₂, 6₁, 7₂ | 2–4 | exact | exact |
| 10₁₀₀ | 14 | **TIMEOUT > 600s** | **exact, 7.2s** |
| 11a1 | 17 | **TIMEOUT > 600s** | identification fails |

**Route 76 is strictly more rigorous and strictly less far-reaching.** It is fully
symbolic — no LLL, no height cap, no precision gate, so Route 75's gate-G2 artifact risk
cannot arise — but on this set it reaches *fewer* manifolds, and in particular fails on
the one (10₁₀₀, degree 14) that Route 75 handles in seconds.

**I set the wrong expectation.** Earlier entries in this bean, and the Route 75/PR text,
read as though the Ptolemy route would "clear both of Route 75's measured ceilings at
once". It does not. Garoufalidis–Goerner–Zickert's "feasible even for many simplices" is
a comparison **against the gluing equations**, which are worse still — not an absolute
claim, and not a promise about 14 tetrahedra.

**Caveat, stated so this is not over-read the other way.** This measures *this
configuration*: 600s budget, `minAssGTZ` rather than `primdecGTZ`, `dp` ordering, default
options, single core. It is **not** a claim that the Ptolemy route cannot reach these
manifolds. Trying `primdecGTZ`, other orderings, and a longer budget is the obvious next
step and is not done.

### Standing conclusion

Use **both**, for different purposes:

- **Route 76** where rigour matters most and the manifold is small — it is float-free end
  to end and needs no artifact gate.
- **Route 75** for reach — it verifies to 14 tetrahedra and degree 14.

And G5 makes them mutually checking, which is worth more than either alone.

---
**2026-08-10 — `finduni` is the right tool, and the 600s "ceiling" was mostly my choice
of algorithm.**

Full primary decomposition is overkill when all you want is the **field**. The Ptolemy
ideals here are **zero-dimensional** (`dim(std(I)) = 0` in every case checked), and for a
zero-dimensional ideal Singular's `finduni` returns the univariate generator per variable
directly. Measured:

| manifold | vars | `minAssGTZ` | `finduni` |
|---|---|---|---|
| 6₁ | 5 | ran | **2.0s**, quartic |
| 7₂ | 5 | ran | **0.0s**, quintic |
| 8₂ | 7 | (not attempted) | **0.0s**, **degree 8** |

`finduni` needs `option(redSB)` — it errors with *"The ideal G has to be reduced"*
otherwise, which is easy to misread as the ideal being unsuitable rather than the basis
being unreduced.

So the earlier "Ptolemy times out at 600s" figure was substantially **a property of
`minAssGTZ`**, not of the Ptolemy route. That tempers the previous entry's reach table in
the *other* direction from the one before it.

**⚠ 10₁₀₀ and 11a1 remain UNMEASURED under `finduni`.** Two attempts were lost to the
same avoidable mistake: a `nohup`-ed job whose parent shell exited, reporting the
wrapper's exit 0 while python had been killed — the trap already recorded in this lane
for `lake` wrappers, repeated here. Re-running under harness-tracked background. Until it
returns, **no claim either way** about whether the Ptolemy route reaches 14 tetrahedra.

---
**2026-08-10 — correcting the previous entry: the job was NOT killed. It is still running.**

The entry above says two `finduni` attempts "were lost … reporting the wrapper's exit 0
while python had been killed". **Half of that is right and the conclusion is wrong.**

Checked with `ps`: the process is alive and has been the whole time —

    2406  python3 finduni_reach.py
    2410  Singular -q --no-warn …    21:12 CPU

It had already written 6₁, 7₂ and 8₂ to its log and was working on **10₁₀₀**, which had
consumed **over twenty minutes of CPU** in `finduni` alone.

- **Right:** the harness's "completed (exit code 0)" was the *wrapper's* exit status, not
  python's — `nohup … &` plus `echo` returns immediately while the child runs detached.
  That part of the standing lesson holds and is worth keeping.
- **Wrong:** inferring from that that the work had been *lost*. It had not. An empty
  output file plus a wrapper's exit code is **not** evidence the job died, any more than
  it is evidence the job succeeded. It is evidence of nothing, and I read it as a
  diagnosis twice.

The correct move on an empty log from a detached job is to **look for the process**
before concluding anything about it. `ps` answers in one call what I guessed at twice.

**Consequence for the reach question.** 10₁₀₀ under `finduni` is genuinely expensive —
20+ minutes of CPU without returning, against 0.0s for 8₂ at degree 8. So the earlier
suggestion that `finduni` simply dissolves the ceiling is **not** supported: it moves it
(degree 8 is now instant where `minAssGTZ` struggled), but 14 tetrahedra remains hard by
this route. Awaiting the timeout to record the number honestly rather than guessing a
third time.

---
**2026-08-10 — 10₁₀₀ MEASURED under `finduni`: still a timeout. The ceiling is real.**

    10_100: 15 Ptolemy variables -> finduni TIMEOUT after 1500s

Measured, not inferred. So switching `minAssGTZ` → `finduni` **moves** the ceiling
without **rescuing** 14 tetrahedra:

| manifold | `minAssGTZ` | `finduni` | Route 75 |
|---|---|---|---|
| 6₁, 7₂ | ran | 2.0s / 0.0s | exact |
| 8₂ (degree 8) | not attempted | **0.0s** | exact |
| 10₁₀₀ (14 tets) | timeout 600s | **timeout 1500s** | **exact, 7.2s** |
| 11a1 (17 tets) | timeout 600s | stopped, not measured | identification fails |

**G6's conclusion stands and is now properly evidenced:** the Ptolemy route is strictly
more rigorous and strictly less far-reaching than Route 75. Recorded in the probe.

11a1 was stopped rather than measured — Route 75 fails on it too, so neither route reaches
it and the number would not change any decision. Said here rather than left implied.

**Standing recommendation, unchanged:** use both. Route 76 where rigour matters and the
manifold is small; Route 75 for reach; G5's field agreement makes them mutually checking.

---
**2026-08-15 — all three deliverables are met. Setting completed.**

Checked this bean's own "What to produce" list rather than assuming, since the entries
below were written across several sessions:

| deliverable | status |
|---|---|
| 1. verdict on the novelty assessment | **CONFIRMED** against both primary sources; G7's quote is real and cited correctly, so no correction to `m015` or the probe docstring |
| 2. priced plan + can it run without Sage/Magma | **yes** — Magma is proprietary and unnecessary; the step both papers use it for is primary decomposition, which is Singular's `minAssGTZ`. `apt-get install singular`, no network, no Sage |
| 3. if it runs: extend Route 75 or open a Route 76 | **Route 76 opened** — `computations/probes/qbeta_route76_ptolemy_singular_probe.py`, 6 gates, with the monomial map recorded in the docstring |

The reach question is measured rather than argued: `finduni` **moves** the ceiling (degree
8 goes from struggling to instant) without **rescuing** 14 tetrahedra — `10₁₀₀` times out
at 600 s under `minAssGTZ` and again at 1500 s under `finduni`, against 7.2 s exact for
Route 75. So G6's conclusion stands with evidence behind it: **the Ptolemy route is
strictly more rigorous and strictly less far-reaching.**

Standing recommendation, unchanged: use both. Route 76 where rigour matters and the
manifold is small; Route 75 for reach; G5's field agreement (`nfisisom` on four cases,
different minimal polynomials, matching discriminants) makes them mutually checking.

### The two lessons this bean produced, kept because both nearly cost a false record

- **A PDF grep proves nothing about a PDF.** Searching both papers for `[Gg]r[oö]bner`
  returned **zero hits** — the extractor renders it `Gr¨ obner`. I nearly recorded a
  misattributed citation on that. Search a diacritic-free substring (`bner`,
  `impractical`) before concluding a source lacks a phrase.
- **An empty log from a detached job is evidence of nothing.** Not that it died, not that
  it succeeded. `ps` answers in one call what I guessed at twice — and the job was alive
  with 21 minutes of CPU while I was writing that it had been killed.
