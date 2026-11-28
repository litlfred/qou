# Evidence, Multi-Database Provenance, and Relevancy Audit: Twisted/Adjoint Reidemeister Torsion, Bring's $(2,4,5)$ Tessellation, Reeb/Garside Geodesic Stepping, and Non-Abelian Stokes (`2026-11-28`)

**Epic:** `qou-s028` (Stability & Foreground Research Evidence Base, supporting Sibling 7 and Sibling 12)
**Branch:** `claude/kg-evidence-ingest-torsion-reeb-stokes-20261128`
**Timestamp (UTC):** `2026-11-28T12:24:50Z` – `2026-11-28T12:34:00Z`
**Authoritative Databases Queried:**
- Crossref REST API (`https://api.crossref.org/works/<DOI>?mailto=...` and bibliographic search)
- arXiv Atom API (`https://export.arxiv.org/api/query`) and e-print source archive (`https://export.arxiv.org/e-print/<id>`, inspected in `/tmp/` only; zero third-party `.pdf` binaries committed per the `2026-11-24` public-repository ruling)
- OpenAlex Works API (`https://api.openalex.org/works/https://doi.org/<DOI>`) and Mathematical Sciences Publishers / AMS / EMS open-access full texts
- Tracked QOU `library/` L1 extractions (`structure.json`, `candidates.json`, `sections/*.md`)

---

## 1. Executive Summary & Anti-Hallucination Audit Findings

To ground QOU's two active mathematical-physics research bridges — **(Topic Area 1)** *Twisted/Adjoint Reidemeister Torsion, Layered Ideal Triangulations, and 1-Loop State-Integral / 3d-Index Saddle Prefactors* and **(Topic Area 2)** *Bring's $(2,4,5)$ Tessellation, Reeb/Beltrami Contact Hydrodynamics, Garside/Template Geodesic Stepping, and Non-Abelian Stokes* — **28 primary works** across pure topology, hyperbolic geometry, $3\text{d}$ $\mathcal{N}=2$ gauge theory, topological hydrodynamics, and $2\text{d}$/$4\text{d}$ gauge holonomy were audited against Crossref, arXiv, and OpenAlex:

1. **15 missing primary references ingested** as schema-validated `folio-reference/v1` nodes in `folio/references/<id>.json`, registered in `folio/schema/references.ts`, exported to `references.bib`, and paired with `qa-attestations/v1` (`bib-verification`) provenance & relevancy records via `writeSourceLedger`:
   - **Topic Area 1 (7 new):** `porti1997`, `dubois2005`, `dubois2006`, `kitano1996`, `muller1993`, `gueritaud2006`, `agol2011`.
   - **Topic Area 2 (8 new):** `weber2005`, `birman-williams1983`, `garside1969`, `birman-ko-lee1998`, `dehornoy2015`, `gaiotto-moore-neitzke2013`, `etnyre-ghrist2000`, `bralic1980`.
2. **3 incomplete pre-existing references upgraded with verified publisher metadata** (preserving existing keys and `library/` links, with zero `bib-human-review` hash invalidation):
   - `ghys2007` (added Crossref DOI `10.4171/022-1/11`, publisher EMS Press, and verified ICM Vol. I pagination `247-277`, replacing an unverified-placeholder note);
   - `arxiv-1204.4824v2` (upgraded from preprint stub to *Annales Henri Poincaré* **14**(7) (2013), `1643-1731`, DOI `10.1007/s00023-013-0239-7`);
   - `dubois2007` (upgraded from preprint stub to *Journal of Knot Theory and Its Ramifications* **18**(3) (2009), `303-341`, DOI `10.1142/S0218216509006951`, with normalized UTF-8 author names).
3. **5 previously unattested core pre-existing references backfilled in `test/attestations/bib-verification/reference/`:** `andersen-kashaev2014`, `dimofte-gaiotto-gukov2014`, `ohtsuki-takata-2015`, `ghys2007`, and `moffatt1969` (total **20 new `bib-verification` attestation files** written via platform `writeSourceLedger`).
4. **6 candidate identifier collisions caught and corrected before ingestion by live API checks** (confirming why unverified arXiv/DOI strings must never enter `folio/references/`):
   - **Faddeev–Kashaev (1994):** candidate `hep-th/9310072` is *The super self-dual matreoshka*; the true Faddeev–Kashaev e-print is `hep-th/9310070` (already held on `faddeev_kashaev1994`, DOI `10.1142/S0217732394000447`).
   - **Dubois (2005):** candidate DOI `10.5802/aif.2137` is Błocki (*Weak solutions to the complex Hessian equation*) and `math/0309272` is a $K3$ paper; the true *Ann. Inst. Fourier* **55**(5), 1685–1734 record is DOI `10.5802/aif.2136` and `arXiv:math/0403470`.
   - **Müller (1993):** AMS JAMS check digit is `-4` (`10.1090/S0894-0347-1993-1189689-4`), not `-1` (HTTP 404).
   - **Agol (2011):** candidate `arXiv:1006.2981` is an ecology preprint and `10.1090/conm/560/11086` is HTTP 404; the true *Contemp. Math.* 560 record is DOI `10.1090/conm/560/11087` and `arXiv:1008.1606`.
   - **Dehornoy et al. (2015):** candidate `arXiv:1310.4909` is a text-classification paper; *Foundations of Garside Theory* is DOI `10.4171/139` and `arXiv:1309.0796`.
   - **Etnyre–Ghrist (2000):** candidate `arXiv:math/0003201` is a quadric-net instanton paper; *Contact topology and hydrodynamics: I* (DOI `10.1088/0951-7715/13/2/306`) has arXiv preprint `arXiv:dg-ga/9708011` (with Part II at `math/9907112` and Part III *knotted flowlines* at `math-ph/9906021`).

---

## 2. Master Provenance Inventory (`folio/references/` + `library/` + Authoritative DBs)

| Reference Key | Status | Topic | Year | Verified DOI | Verified arXiv / OA | `library/` Dir | DB Source (`2026-11-28Z`) |
|---|---|---|---:|---|---|---|---|
| `porti1997` | **NEW** | T1 | 1997 | `10.1090/memo/0612` | — | — | Crossref + OpenAlex |
| `porti2015` | Pre-existing | T1 | 2015 | — (preprint survey) | `arXiv:1511.00400v2` | `library/arxiv-1511.00400v2` | `library/` + arXiv |
| `dubois2005` | **NEW** | T1 | 2005 | `10.5802/aif.2136` | `arXiv:math/0403470v4` | — | Crossref + arXiv e-print |
| `dubois2006` | **NEW** | T1 | 2006 | `10.4153/cmb-2006-006-0` | `arXiv:math/0403304v2` | — | Crossref + arXiv e-print |
| `dubois2007` | **UPGRADED** | T1 | 2009 | `10.1142/S0218216509006951` | `arXiv:0706.2213v3` | `library/arxiv-0706.2213v3` | Crossref + arXiv + `library/` |
| `kitano1996` | **NEW** | T1 | 1996 | `10.2140/pjm.1996.174.431` | MSP Open Access | — | Crossref + OpenAlex + MSP |
| `muller1993` | **NEW** | T1 | 1993 | `10.1090/S0894-0347-1993-1189689-4` | AMS Open Access | — | Crossref + OpenAlex |
| `andersen-kashaev2014` | Pre-existing (+Attest) | T1/T2 | 2014 | `10.1007/s00220-014-2073-2` | `arXiv:1109.6295v2` | — | Crossref + arXiv e-print |
| `dimofte-gaiotto-gukov2014` | Pre-existing (+Attest) | T1 | 2014 | `10.1007/s00220-013-1863-2` | `arXiv:1108.4389v1` | `library/arxiv-1108.4389v1` (`dimofte-gaiotto2011`) | Crossref + arXiv + `library/` |
| `dimofte-gaiotto-gukov2013` | Pre-existing | T1 | 2013 | `10.4310/ATMP.2013.v17.n5.a3` | `arXiv:1112.5179v1` | `library/arxiv-1112.5179v1` | Crossref + arXiv + `library/` |
| `dimofte-garoufalidis-2013` | Pre-existing | T1 | 2013 | `10.2140/gt.2013.17.1253` | `arXiv:1202.6268v2` | `library/arxiv-1202.6268v2` | Crossref + arXiv + `library/` |
| `ohtsuki-takata-2015` | Pre-existing (+Attest) | T1 | 2015 | `10.2140/gt.2015.19.853` | RIMS-1785 / MSP | — | Crossref |
| `garoufalidis-yoon-2024` | Pre-existing | T1 | 2024 | — (preprint) | `arXiv:2411.03801v2` | `library/arxiv-2411.03801v2` | `library/` |
| `garoufalidis-zagier2023` | Pre-existing | T1 | 2023 | `10.3842/SIGMA.2023.082` | `arXiv:2304.09377v2` | `library/arxiv-2304.09377v2` | Crossref + arXiv + `library/` |
| `garoufalidis-zagier-2024` | Pre-existing | T1 | 2024 | `10.3842/SIGMA.2024.055` | `arXiv:2111.06645v3` | `library/arxiv-2111.06645v3` | Crossref + arXiv + `library/` |
| `gueritaud2006` | **NEW** | T1/T2 | 2006 | `10.2140/gt.2006.10.1239` | `arXiv:math/0406242v4` | — (`futer-gueritaud-angled` survey held) | Crossref + arXiv e-print |
| `agol2011` | **NEW** | T1/T2 | 2011 | `10.1090/conm/560/11087` | `arXiv:1008.1606v2` | — | Crossref + arXiv e-print |
| `weber2005` | **NEW** | T2 | 2005 | `10.2140/pjm.2005.220.167` | MSP Open Access | — | Crossref + OpenAlex + MSP |
| `riera-rodriguez-1992` | Pre-existing | T2 | 1992 | `10.2140/pjm.1992.154.179` | MSP Open Access | `library/pjm-v154-n1-p09-s` | Crossref + `library/` |
| `birman-williams1983` | **NEW** | T2 | 1983 | `10.1016/0040-9383(83)90045-9` | — | — | Crossref + OpenAlex |
| `ghys2007` | **UPGRADED** (+Attest) | T2 | 2007 | `10.4171/022-1/11` | ENS Lyon / EMS OA | — | Crossref + OA full text |
| `garside1969` | **NEW** | T2 | 1969 | `10.1093/qmath/20.1.235` | — | — | Crossref |
| `birman-ko-lee1998` | **NEW** | T2 | 1998 | `10.1006/aima.1998.1761` | `arXiv:math/9712211v2` | — | Crossref + arXiv e-print |
| `dehornoy2015` | **NEW** | T2 | 2015 | `10.4171/139` | `arXiv:1309.0796v1` | — | Crossref + arXiv e-print |
| `gaiotto-moore-neitzke2013` | **NEW** | T2 | 2013 | `10.1016/j.aim.2012.09.027` | `arXiv:0907.3987v2` | — | Crossref + arXiv e-print |
| `arxiv-1204.4824v2` | **UPGRADED** | T2 | 2013 | `10.1007/s00023-013-0239-7` | `arXiv:1204.4824v2` | `library/arxiv-1204.4824v2` | Crossref + arXiv + `library/` |
| `faddeev_kashaev1994` | Pre-existing | T1/T2 | 1994 | `10.1142/S0217732394000447` | `arXiv:hep-th/9310070v1` | `library/arxiv-hep-th-9310070v1` | Crossref + arXiv + `library/` |
| `etnyre-ghrist2000` | **NEW** | T2 | 2000 | `10.1088/0951-7715/13/2/306` | `arXiv:dg-ga/9708011v1` | — | Crossref + arXiv e-print |
| `moffatt1969` | Pre-existing (+Attest) | T2 | 1969 | `10.1017/S0022112069000991` | — | `library/moffatt1969-jfm-knottedness` | Crossref + `library/` |
| `bralic1980` | **NEW** | T2 | 1980 | `10.1103/PhysRevD.22.3090` | — | — | Crossref + OpenAlex |
| `yekutieli2015` | Pre-existing | T2 | 2015 | `10.1142/9537` | `arXiv:1007.1250v4` | `library/arxiv-1007.1250v4` | `library/` |

---

## 3. Topic Area 1 — Twisted/Adjoint Reidemeister Torsion, Layered Tetrahedra & 1-Loop State-Integral Saddle Prefactors

### 3.1 Architectural Bridge in QOU (Supporting Sibling 12)

The Topic Area 1 chain connects combinatorial braid/Farey data to exact 1-loop hyperbolic invariants and Stokes matrices:

$$\text{Farey / pseudo-Anosov word } \Omega \;\xrightarrow{\text{Guéritaud / Agol}}\; \text{Layered / veering ideal triangulation } \{\Delta_i\}_{i=1}^N \;\xrightarrow{\text{Faddeev–Kashaev / AK / DGG}}\; \begin{cases} \mathcal{Z}_\hbar(M) = \int \prod_i \Phi_b(z_i)\,dx & \text{(state integral)} \\ I_M(m,e;q) = \sum \prod_i I_\Delta & \text{(rotated } 3\text{d index)} \end{cases}$$

At the geometric saddle $z_i = z_i^{\mathrm{geom}}$ as $\hbar \to 0$, the Gaussian Hessian determinant $\det(A z^{-1} + B (1-z)^{-1})$ is governed by the Neumann–Zagier symplectic matrix $(A \mid B)$ and matches the non-abelian $\mathrm{Ad}\circ\rho_{\mathrm{geom}}$ Reidemeister torsion $\tau_{\mathrm{Ad}}(M; \gamma)$ (Porti, Dubois, Dimofte–Garoufalidis, Ohtsuki–Takata, Garoufalidis–Yoon, Garoufalidis–Zagier).

### 3.2 Per-Paper Evidence, Exact Locators, and Claim Boundaries (Topic Area 1)

#### 1. `porti1997` — Joan Porti (1997), *Torsion de Reidemeister pour les variétés hyperboliques*
- **Provenance:** Mem. Amer. Math. Soc. **128**, no. 612 (1997), x+139 pp.; DOI `10.1090/memo/0612` (`claim_domain: math`, `evidence_location: elsewhere`).
- **Exact Locators:** §3.1.3 & Corollary 3.23 (canonical homological basis for $\mathrm{Ad}\circ\rho$-twisted cohomology $H^*(M; \mathfrak{sl}_2(\mathbb{C})_{\mathrm{Ad}\circ\rho}) \cong \bigoplus_{i=1}^c H^*(T_i^2; \mathbb{C})$ at $\gamma$-regular representations); Proposition 4.10 & Corollary 4.18 (change-of-peripheral-curve Jacobian $\mathbb{T}_{(M,\gamma_1)}(\rho)/\mathbb{T}_{(M,\gamma_2)}(\rho) = \det(\partial u_{\gamma_1}/\partial u_{\gamma_2})$ and behavior under hyperbolic Dehn filling).
- **What It Proves for QOU:** Supplies the rigorous definition of peripheral-curve-framed adjoint $\mathrm{SL}_2(\mathbb{C})$ Reidemeister torsion on one-cusped and multi-cusped hyperbolic $3$-manifolds ($4_1$, $5_2$, Whitehead $L5a1$, Borromean $L6a4$) and proves that switching from meridian $\mu$ to longitude $\lambda$ multiplies $\tau_{\mathrm{Ad}}$ by the $A$-polynomial logarithmic derivative $\pm \tfrac{1}{2} d\log M / d\log L$ (`prop:fivetwo-stokes-unimodular`, `docs/audits/2026-08-07-probe-c4-bring-adjoint-torsion-framing.md`).
- **Claim Boundary:** Purely classical/cohomological invariant on the $\mathrm{SL}_2(\mathbb{C})$ character variety; proves **nothing** about quantum dilogarithm state integrals, colored Jones asymptotics, or closed surfaces $\Sigma_4$ without choosing an acyclic flat $\mathrm{SL}_2(\mathbb{C})$ bundle.

#### 2. `dubois2005` — Jérôme Dubois (2005), *Non abelian Reidemeister torsion and volume form on the $SU(2)$-representation space of knot groups*
- **Provenance:** Ann. Inst. Fourier **55**(5) (2005), 1685–1734; DOI `10.5802/aif.2136`; `arXiv:math/0403470v4` (`claim_domain: math`, `evidence_location: elsewhere`).
- **Exact Locators:** §3–4, Proposition 3.5 (`propmureg`, characterization of $\mu$-regularity); Proposition 4.1 (`P:TorsionAlexander`, limit at abelian representations recovering Alexander torsion); §6–7, Main Theorem / Theorem 7.1 (`T:Volume=Torsion`: $\tau^K_\rho = \mathrm{vol}^K_{[\rho]}$ on regular $\mathrm{SU}(2)$ representations).
- **What It Proves for QOU:** Pins the sign ambiguity of Porti's non-abelian torsion via Turaev Euler structures + homology orientations and identifies the resulting sign-determined torsion with the symplectic Casson–Lin–Heusener volume form on the $\mathrm{SU}(2)$ character variety — grounding the "torsion = topological measure/density on flat connections" step in QOU's 1-loop saddle-weight interpretation.
- **Claim Boundary:** Proved for compact $\mathrm{SU}(2)$ representations of knot exteriors in $S^3$; complexification to the non-unitary geometric $\mathrm{PSL}_2(\mathbb{C})$ holonomy requires analytic continuation along the character curve (`porti1997`, `dubois2007`).

#### 3. `dubois2006` — Jérôme Dubois (2006), *Non Abelian Twisted Reidemeister Torsion for Fibered Knots* & `dubois2007` — Dubois, Huynh, & Yamaguchi (2009)
- **Provenance:** `dubois2006`: Canad. Math. Bull. **49**(1) (2006), 55–71, DOI `10.4153/cmb-2006-006-0`, `arXiv:math/0403304v2`; `dubois2007`: J. Knot Theory Ramifications **18**(3) (2009), 303–341, DOI `10.1142/S0218216509006951`, `arXiv:0706.2213v3` (`claim_domain: math`).
- **Exact Locators:** `dubois2006` §3 Main Theorem & §5 Examples (computes $\mathbb{T}^K_\mu(\rho)$ of fibered knots directly from the monodromy action on the Punctured-Surface fiber group, evaluating torus knots $T(2,2k+1)$ and figure-eight $4_1$); `dubois2007` §3–4, Propositions 1–2 (recursive character-variety and non-abelian torsion formulas across all twist knots $K_p$, covering $4_1$ and $5_2 = K_2$).
- **What It Proves for QOU:** Gives independent closed-form algebraic evaluations of $\tau_{\mathrm{Ad}}$ on both QOU cross-knot anchors: $4_1$ ($\sqrt{3}$ / discriminant $-3$, fibered) and $5_2$ (non-fibered twist knot, cubic trace field $\theta^3 - \theta + 1 = 0$ of discriminant $-23$).
- **Claim Boundary:** `dubois2006`'s monodromy determinant formula requires fiberedness (so it covers $4_1$ and torus knots $T(2,p)$, **not** $5_2$); $5_2$ requires `dubois2007`'s Fox-calculus twist-knot recursion or `porti1997`.

#### 4. `kitano1996` — Teruaki Kitano (1996), *Twisted Alexander polynomial and Reidemeister torsion* & `muller1993` — Werner Müller (1993), *Analytic torsion and $R$-torsion for unimodular representations*
- **Provenance:** `kitano1996`: Pacific J. Math. **174**(2) (1996), 431–442, DOI `10.2140/pjm.1996.174.431`; `muller1993`: J. Amer. Math. Soc. **6**(3) (1993), 721–753, DOI `10.1090/S0894-0347-1993-1189689-4` (`claim_domain: math`).
- **Exact Locators:** `kitano1996` Theorem A (§3, $\Delta_{K,\rho}(t) = \tau(E_K; \rho \otimes \alpha)$ for acyclic $\mathrm{SL}_n$-representations) and Theorem B (§4, reciprocity $\Delta_{K,\rho}(t) = \Delta_{K,\rho}(t^{-1})$ up to $t^{mn}$ for $\mathrm{SO}(n)$); `muller1993` Theorem 1 (equality of Ray–Singer analytic torsion and combinatorial Reidemeister torsion for unimodular $\mathrm{SL}_n(\mathbb{C})$ representations on closed odd-dimensional manifolds).
- **What It Proves for QOU:** `kitano1996` bridges combinatorial Fox-calculus Alexander determinants (computable over polynomial rings) to Reidemeister torsion; `muller1993` bridges combinatorial Reidemeister torsion to spectral $\zeta$-regularized Laplace determinants for non-unitary $\mathrm{SL}_n(\mathbb{C})$ representations.
- **Claim Boundary:** `muller1993` requires **closed** odd-dimensional manifolds and acyclic unimodular representations — cusped knot complements require cusp truncation / Dehn-surgery anomaly control (supplied later by Park / Porti / Menal-Ferrer–Porti), and closed surfaces like $\Sigma_4$ have $\dim = 2$ (even), where classical $R$-torsion is trivial unless lifted to a $3$-manifold bundle such as $\mathrm{UT}(\Sigma_4)$.

#### 5. `gueritaud2006` — François Guéritaud (2006, with Appendix by David Futer) & `agol2011` — Ian Agol (2011)
- **Provenance:** `gueritaud2006`: Geom. Topol. **10**(3) (2006), 1239–1284, DOI `10.2140/gt.2006.10.1239`, `arXiv:math/0406242v4`; `agol2011`: Contemp. Math. **560** (2011), 1–17, DOI `10.1090/conm/560/11087`, `arXiv:1008.1606v2` (`claim_domain: math`).
- **Exact Locators:** `gueritaud2006` §2–8 Theorem 1.1 (`main`, positive angle structures and Rivin volume concavity on layered punctured-torus bundles from $RL$ words) and §9–10 (Futer's Appendix B: canonical geometric ideal triangulations of hyperbolic two-bridge links from Farey words + pillowcase foldings); `agol2011` §3 Theorem 3.5 (`periodicsplitting`) & §4 Proposition 4.2 (`veering`: periodic train-track splitting of any punctured pseudo-Anosov mapping torus yields a canonical veering taut ideal triangulation via Whitehead flips).
- **What It Proves for QOU:** Directly underpins `docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md`, `QOU/Mass/FiveTwoGluingFromFareyWord.lean`, and `QOU/Transcendental/BraidKnotOctonion/RivinConcavity.lean`: every letter $R$ or $L$ of a Farey / train-track stepping word inserts a concrete tetrahedral diagonal flip, producing the exact $2$-tetrahedron ($4_1$, word `R`) and $4$-tetrahedron / SnapPy `m015` ($5_2$, word `RL`) Neumann–Zagier matrices without fitting.
- **Claim Boundary:** `gueritaud2006` covers once-punctured torus bundles and hyperbolic two-bridge links; `agol2011` covers punctured pseudo-Anosov mapping tori ($4_1$ is fibered so both apply; $5_2$ is non-fibered two-bridge so `gueritaud2006` §9–10 applies while `agol2011` does not). Non-hyperbolic torus knots ($T(2,p)$) have empty positive-angle polytopes and zero hyperbolic volume.

#### 6. `andersen-kashaev2014`, `dimofte-gaiotto-gukov2014`, `dimofte-gaiotto-gukov2013`, `dimofte-garoufalidis-2013`, `ohtsuki-takata-2015`, `garoufalidis-yoon-2024`, `garoufalidis-zagier2023`, `garoufalidis-zagier-2024`
- **Exact Locators Verified:**
  - `andersen-kashaev2014` (`1109.6295`): §4 Proposition 3 (`charged-pentagon`), §6 Theorem 4 (`Main`, state-integral TQFT functor from shaped $2$–$3$ Pachner moves), §10 Theorem 5 (`th:4-1--5-2`, rigorous convergence and explicit state integrals for $(S^3, 4_1)$ and $(S^3, 5_2)$).
  - `dimofte-gaiotto-gukov2014` (`1108.4389`) & `dimofte-gaiotto-gukov2013` (`1112.5179`): `2014` §3–4 ($\mathrm{Sp}(2N,\mathbb{Z})$ polarization transformations of $3\text{d}$ $\mathcal{N}=2$ class $\mathcal{R}$ theories $T_M$ matching Neumann–Zagier gluing, with $2$–$3$ Pachner invariance realized as SQED $\leftrightarrow XYZ$ mirror symmetry = Faddeev's pentagon); `2013` §4.1–4.3 (tetrahedron index $I_\Delta(m,e;q)$, triality §4.3, and internal-edge flux summation).
  - `dimofte-garoufalidis-2013` (`1202.6268`): §1.2 Theorem 1.1 & §3 (`The 1-loop invariant` $\tau_M^{\mathrm{NZ}} = \pm \tfrac{1}{2}\det(A z^{-1} + B (1-z)^{-1})$ from Neumann–Zagier matrices, conjectured equal to Reidemeister torsion).
  - `ohtsuki-takata-2015` (DOI `10.2140/gt.2015.19.853`) & `garoufalidis-yoon-2024` (`2411.03801`): `ohtsuki-takata-2015` Theorem 1.1 ($\omega(D)^2 = \pm T(K)/(2\sqrt{-1})$ relating Kashaev 1-loop saddle prefactor to twisted Reidemeister torsion for two-bridge diagrams); `garoufalidis-yoon-2024` Theorem 1.1 (proves Dimofte–Garoufalidis 1-loop $\tau_M^{\mathrm{NZ}} = \pm \tau_{\mathrm{Ad}}(K)$ unconditionally for **all hyperbolic two-bridge knots**, covering $4_1$, $5_2$, and $6_2$).
  - `garoufalidis-zagier2023` (`2304.09377`, SIGMA 19:082) & `garoufalidis-zagier-2024` (`2111.06645`, SIGMA 20:055): `2023` §2.3–2.4 & Theorem 5.2 (holomorphic $q$-series $G_0(q), G_1(q)$ from state integrals and rotated 3d index); `2024` Part I §1.4–1.6 & Propositions 8.1, 10.1–10.2 (matrix-valued perturbative series $\Phi_\alpha^{(\sigma)}(h)$ indexed by flat connections $\alpha$, Stokes matrices, and quantum modularity at roots of unity).
- **What This Cluster Proves for QOU:** Certifies that (i) the 1-loop NZ determinant of $4_1$, $5_2$, and $6_2$ equals adjoint Reidemeister torsion (`garoufalidis-yoon-2024`), (ii) the $4_1$ and $5_2$ state integrals are topological invariants under leveled $3$–$2$ moves (`andersen-kashaev2014` Theorem 5), and (iii) the rotated 3d index $I_M(m,e;q)$ carries integer BPS/Donaldson–Thomas counts from which QOU's `TetIndexTriality.lean` and `StokesIndexCount52.lean` extract the $4_1$ Stokes constant $3$ unconditionally and the $5_2$ $q^0$ Stokes constants $4, -3, -9$.
- **Claim Boundary:** (a) Full all-orders Kashaev Volume Conjecture is rigorous up to $\le 7$ crossings (`ohtsuki2016`), not general knots; (b) in `2026-11-28-fivetwo-stokes-from-3d-index.md`, the $5_2$ holomorphic-block bilinear $\leftrightarrow$ `m015` 3d-index identity is verified numerically to $40$ digits and relies on Garoufalidis–Gu–Mariño's region-matrix ansatz, whereas only the $q^0$ Stokes gauge/factorisation (`StokesIndexCount52.lean`) and $4_1$ triality/degree bounds (`TetIndexTriality.lean`) are currently machine-proved in Lean.

---

## 4. Topic Area 2 — Bring's $(2,4,5)$ Tessellation, Reeb/Garside Stepping, Contact Hydrodynamics & Non-Abelian Stokes

### 4.1 Architectural Bridge in QOU (Supporting Sibling 7)

Topic Area 2 links the conformal/hyperbolic geometry of Bring's genus-$4$ surface $\Sigma_4$ and its unit tangent bundle $M = \mathrm{UT}(\Sigma_4)$ to braid stepping, contact hydrodynamics, and surface-ordered non-abelian Stokes:

1. **Surface & Period Geometry:** Kepler's small stellated dodecahedron carries the $\{5,4\}$ / $(2,4,5)$ hyperbolic tessellation presenting Bring's curve $\Sigma_4$ with $\mathrm{Aut}(\Sigma_4) = S_5$, $\chi(\Sigma_4) = -6$, and $\mathrm{Jac}(\Sigma_4) \sim E^4$ (`weber2005`, `riera-rodriguez-1992`, `braden-northover-2012`).
2. **Unit Tangent Bundle, Contact Reeb Flow & Beltrami Hydrodynamics:** The link of Bring's canonical cone is $M = \mathrm{UT}(\Sigma_4) \cong \Gamma\backslash\mathrm{PSL}_2(\mathbb{R})$ (`lem:bring-cone-reeb-quaternionic-twist`). Its fiber-rotation field $V$ is both a Boothby–Wang contact Reeb vector field and a non-singular rotational Beltrami steady Euler flow (`etnyre-ghrist2000`, `prop:reeb-beltrami-regular-flow`), while filament linking/knottedness defines classical fluid helicity (`moffatt1969`, `prop:helicity-conservation`).
3. **Template Reduction & Garside Normal-Form Geodesic Stepping:** Periodic orbits of hyperbolic/geodesic $3$-flows project to branched $2$-manifold templates carrying positive braid words (`birman-williams1983`, `ghys2007`), where Garside and dual Birman–Ko–Lee normal forms define canonical minimal-step geodesic decompositions (`garside1969`, `birman-ko-lee1998`, `dehornoy2015`).
4. **Non-Abelian Surface Stokes & Quantum Dilogarithm Pentagon:** Across a $2$-dimensional worldsheet or WKB spectral network, boundary holonomy $\mathcal{P}\exp\oint_{\partial S} A$ factorizes into a surface-ordered curvature integral (`bralic1980`, `yekutieli2015`), while discrete triangulation flips across Stokes walls conjugate flat/quantum coordinates by Faddeev's $\Phi_b$ pentagon identity (`faddeev_kashaev1994`, `gaiotto-moore-neitzke2013`, `arxiv-1204.4824v2`).

### 4.2 Per-Paper Evidence, Exact Locators, and Claim Boundaries (Topic Area 2)

#### 1. `weber2005` — Matthias Weber (2005), *Kepler's small stellated dodecahedron as a Riemann surface* & `riera-rodriguez-1992` — Riera & Rodríguez (1992)
- **Provenance:** `weber2005`: Pacific J. Math. **220**(1) (2005), 167–182, DOI `10.2140/pjm.2005.220.167`; `riera-rodriguez-1992`: Pacific J. Math. **154**(1) (1992), 179–200, DOI `10.2140/pjm.1992.154.179` (`claim_domain: math`, `evidence_location: elsewhere`).
- **Exact Locators:** `weber2005` §2 Lemma 2.1 & Proposition 2.2 (hyperbolic $\{5,4\}$ pentagon tessellation of the small stellated dodecahedron $\mathcal{S}$ with $\mathrm{Aut}(\mathcal{S}) = S_5$), §3–4 Proposition 3.1 (biholomorphism with Bring's curve), §5 Theorem 1.1, Lemma 5.2, Corollary 5.5 ($\mathrm{Jac}(\mathcal{S}) \sim T^4$ for an explicit rhombic torus $T$ via flat cone metrics); `riera-rodriguez-1992` §2 (20-gon $(2,4,5)$ canonical homology basis) and Lemma 1 ($\mathrm{Sp}\Gamma_0(5)$ stabilizer and period matrix $Z = \tau_0 C$).
- **What It Proves for QOU:** Grounds QOU's $(2,4,5)$ vertex/multiplier geometry (`QOU/Archimedean/SigmaJGeometricCarrier.lean`, order-$4$ cone multiplier $\pm i$ at $\{5,4\}$ vertices descending to the elliptic quotient $E_{5\tau_0}$) and the $\mathrm{Jac}(\Sigma_4) \sim E_{5\tau_0}^3 \times E_{\tau_0}$ decomposition (`BringEllipticFactor.lean`, `BringHauptmodulGate.lean`).
- **Claim Boundary:** `riera-rodriguez-1992` contains a known typographical swap between the two elliptic $j$-invariants $j(\tau_0)$ and $j(5\tau_0)$ (flagged by `braden-northover-2012` p. 15 and already corrected in QOU probes); `weber2005` proves the isogeny $\mathrm{Jac}(\Sigma_4) \sim T^4$ geometrically over $\mathbb{C}$ without fixing any physical coupling constant.

#### 2. `birman-williams1983` — Birman & Williams (1983) & `ghys2007` — Étienne Ghys (2007), *Knots and dynamics*
- **Provenance:** `birman-williams1983`: Topology **22**(1) (1983), 47–82, DOI `10.1016/0040-9383(83)90045-9`; `ghys2007`: Proc. ICM (Madrid, 2006), Vol. I, 247–277, DOI `10.4171/022-1/11` (`claim_domain: math`).
- **Exact Locators:** `birman-williams1983` §2–4 (Template Theorem: collapsing local stable manifolds of a hyperbolic chain-recurrent $3$-flow set yields a branched $2$-manifold template embedding periodic orbits isotopically as Lorenz positive braids); `ghys2007` §3.1–3.5 (modular knots = closed geodesics in $\mathrm{UT}(\mathrm{PSL}_2(\mathbb{Z})\backslash\mathbb{H}) \cong S^3 \setminus T_{2,3}$ are isotopic to Lorenz knots on the Birman–Williams template, with trefoil linking number equal to the Rademacher function $\Psi(A)$).
- **What It Proves for QOU:** Establishes rigorously how closed geodesic orbits on unit tangent bundles of hyperbolic orbifolds/surfaces become positive-braid template knots encoded by $\mathrm{SL}_2(\mathbb{Z})$ $RL$ cutting sequences (`rem:braid-fluid`, cat-map / $RL$ lepton and Farey probes).
- **Claim Boundary:** `ghys2007`'s exact isotopy with Lorenz knots in $S^3$ uses $\mathrm{UT}(\mathrm{PSL}_2(\mathbb{Z})\backslash\mathbb{H}) \cong S^3 \setminus T_{2,3}$ (the $(2,3,\infty)$ modular orbifold); for the closed genus-$4$ surface $\Sigma_4$, $\mathrm{UT}(\Sigma_4)$ is a closed rational-homology-nontrivial $3$-manifold ($b_1 = 8$, Euler number $-6$), not a knot complement in $S^3$, so closed geodesics in $\mathrm{UT}(\Sigma_4)$ live in $\mathrm{UT}(\Sigma_4)$ unless pushed down to $S^3$ via an explicit branched covering or surgery map.

#### 3. `garside1969`, `birman-ko-lee1998`, & `dehornoy2015` — Garside & Dual-Garside Geodesic Normal Forms
- **Provenance:** `garside1969`: Quart. J. Math. **20**(1) (1969), 235–254, DOI `10.1093/qmath/20.1.235`; `birman-ko-lee1998`: Adv. Math. **139**(2) (1998), 322–353, DOI `10.1006/aima.1998.1761`, `arXiv:math/9712211v2`; `dehornoy2015`: EMS Tracts in Math. **22**, DOI `10.4171/139`, `arXiv:1309.0796v1` (`claim_domain: math`).
- **Exact Locators:** `garside1969` §1–2 Theorems 1–5 (positive monoid $B_n^+ \hookrightarrow B_n$, half-twist $\Delta$, summit set); `birman-ko-lee1998` §2–3 Theorem 2.6 (`thm:embedding`), Theorem 3.4 (`thm:l canonical form`: unique left-canonical form $W = \delta^u A_1 \cdots A_k$ in band generators $a_{ts}$), Theorem 3.8 (`thm:complexityword`: $O(|W|^2 n)$ word complexity); `dehornoy2015` Ch. II–III (greedy normal-form paths as canonical geodesics in the Cayley graph of simple elements, cycling/sliding).
- **What It Proves for QOU:** Supplies the canonical algebraic normal-form and step-length machinery for braid words in $B_n$, and pairs with Ito (`ito2008`, `2026-08-25-ito-dehornoy-hyperbolicity-criterion.md`) to distinguish genuinely $n$-strand pseudo-Anosov closures from stabilized lower-index braids.
- **Claim Boundary:** Garside normal-form length counts minimal factor steps in the chosen Garside/BKL generating family ($\Delta$-simples or $\delta$-simples), which is distinct from Artin crossing length and from hyperbolic volume unless linked by an explicit train-track / Ito Dehornoy-floor hypothesis ($[\beta]_D \ge 3$).

#### 4. `faddeev_kashaev1994`, `gaiotto-moore-neitzke2013` (`0907.3987`), & `arxiv-1204.4824v2` (`Spectral Networks`)
- **Provenance:** `faddeev_kashaev1994`: Mod. Phys. Lett. A **9**(5) (1994), 427–434, DOI `10.1142/S0217732394000447`, `arXiv:hep-th/9310070v1`; `gaiotto-moore-neitzke2013`: Adv. Math. **234** (2013), 239–403, DOI `10.1016/j.aim.2012.09.027`, `arXiv:0907.3987v2`; `arxiv-1204.4824v2`: Ann. Henri Poincaré **14**(7) (2013), 1643–1731, DOI `10.1007/s00023-013-0239-7` (`claim_domain: math` / mathematical physics).
- **Exact Locators:** `faddeev_kashaev1994` §2–3 (Weyl-pair operator pentagon $S(U) S(V) = S(V) S(VU) S(U)$ for $UV = q VU$ and classical Rogers five-term limit); `gaiotto-moore-neitzke2013` §5.6 (`subsec:TransfmFlips`, cluster coordinate flips), §6.5 (`subsec:Jumps-WKB-triang`, WKB triangulation flips/pops across BPS Stokes walls), §7.7 (Kontsevich–Soibelman dilogarithm symplectomorphisms), §11 (`sec:UniversalStokesMatrix`, spectrum generator $\mathbb{S}$); `arxiv-1204.4824v2` §5 & §10.1–10.3 (spectral-network non-abelianization map between flat abelian connections on branched covers $\Sigma \to C$ and flat $\mathrm{GL}(K,\mathbb{C})$ connections on $C$).
- **What It Proves for QOU:** Provides the exact mathematical-physics mechanism by which discrete flips of an ideal/WKB triangulation act as quantum-dilogarithm / cluster Stokes transformations whose $\hbar \to 0$ limit recovers Rogers's five-term dilogarithm identity (`FiveTwoComplexPentagon.lean`, `prop:mi-sw-abelianisation`).
- **Claim Boundary:** `gaiotto-moore-neitzke2013` and `arxiv-1204.4824v2` require a curve $C$ equipped with a meromorphic Higgs field / quadratic differential $\phi_2$ (or higher differentials for class $\mathcal{S}$) whose zeros are simple or controlled; as recorded in `prop:mi-sw-abelianisation` (`validation: "stub"`), QOU has not yet constructed an explicit spectral cover + fake-flatness instance discharging `MISWAbelianisation` on $\Sigma_4$.

#### 5. `etnyre-ghrist2000`, `moffatt1969`, `bralic1980`, & `yekutieli2015` — Hydrodynamic Reeb/Helicity & Gauge Surface Stokes
- **Provenance:** `etnyre-ghrist2000`: Nonlinearity **13**(2) (2000), 441–458, DOI `10.1088/0951-7715/13/2/306`, `arXiv:dg-ga/9708011v1`; `moffatt1969`: J. Fluid Mech. **35**(1) (1969), 117–129, DOI `10.1017/S0022112069000991`; `bralic1980`: Phys. Rev. D **22**(12) (1980), 3090–3103, DOI `10.1103/PhysRevD.22.3090`; `yekutieli2015`: World Scientific, DOI `10.1142/9537`, `arXiv:1007.1250v4` (`claim_domain: math` / `science` mathematical physics).
- **Exact Locators:**
  - `etnyre-ghrist2000` §2 Theorem 2.1 (`thm_BelReeb`) & Corollary 2.2: any non-singular rotational Beltrami field ($\mathrm{curl}\,u = \lambda u$, $\lambda \neq 0$) on a Riemannian $3$-manifold is a Reeb-like field for a contact form $\alpha$, and conversely any Reeb field of a contact $1$-form generates a steady incompressible Euler solution for a compatible Riemannian metric.
  - `moffatt1969` §2–3 eq. (3.6): inviscid conservation of helicity $I = \int u \cdot \omega\,dV$ and evaluation $I = \sum_{i,j} \alpha_{ij}\kappa_i\kappa_j$ in terms of Gauss linking numbers of discrete vortex filaments.
  - `bralic1980` §II eqs. (2.11)–(2.19) & §III–IV: exact non-abelian surface Stokes formula $\mathcal{P}\exp\oint_{\partial\Sigma} A = \mathcal{P}_s \exp \int_\Sigma U^{-1} F U\,ds\,dt$ for $2\text{d}$ Yang–Mills Wilson loops, yielding exact entangled-loop expectations.
  - `yekutieli2015` Ch. 6–7 (2d multiplicative surface integration and non-abelian Stokes theorem for crossed modules / connection-curvature pairs under fake-flatness).
- **What This Cluster Proves for QOU:**
  1. Gives direct mathematical-physics provenance for `prop:reeb-beltrami-regular-flow` (`QOU/FluidDynamics/BeltramiSteadyEuler.lean`), where the fiber rotation $V$ of $\mathrm{UT}(\Sigma_4)$ is simultaneously the Boothby–Wang contact Reeb field and a rotational Beltrami flow ($\mathrm{curl}(V/s) = -s(V/s)$).
  2. Grounds `prop:helicity-conservation` and `rem:braid-fluid`: classical Moffatt helicity detects only pairwise linking/writhe (order-$1$ Vassiliev data), explaining why the Markov-trace Jones invariant $J_L(q)$ strictly refines classical helicity on unlinked knots.
  3. Connects QOU's algebraic/sheaf-theoretic Yekutieli obstruction (`lem:yekutieli-leading-coefficient`, `ex:archimedean-yekutieli`, `prop:mi-sw-abelianisation`) to standard continuum Yang–Mills Wilson-loop physics (`bralic1980`).
- **Claim Boundary:**
  1. `etnyre-ghrist2000` applies to **steady inviscid Euler** ($\nu = 0$) by choosing a contact-adapted Riemannian metric; for viscous Navier–Stokes ($\nu > 0$) on a **fixed** metric, a Beltrami field decays or remains steady only when it is simultaneously a curl/Laplace eigenfield or Killing field (proved for $V$ on $(\mathrm{UT}(\Sigma_4), g_s)$ in `BeltramiSteadyEuler.lean`, covering only the $1$-parameter ray $a V$ and **not** generic initial data).
  2. `bralic1980` computes exact expectations in **$2$-dimensional** continuum Yang–Mills theory (where the Yang–Mills measure on a surface is quasi-topological / area-preserving); in $4\text{d}$ gauge theory or on curved $3$-manifolds without fake-flatness (`Yekutieli 2015` Ch. 6), surface-ordered holonomy depends on the foliation/parametrization of the spanning surface unless a crossed-module fake-flatness condition holds.

---

## 5. Content Block Wiring Summary

The following four non-conflicting content blocks were enriched with verified `cites: [...]` edges and `authorNotes` provenance & claim-boundary notes (with `.jsonld` siblings regenerated cleanly via `scripts/gen-block-jsonld.sh`):

1. `folio/quantum-observable-universe/fluid-dynamics/reeb-beltrami-regular-flow.ts` (`prop:reeb-beltrami-regular-flow`) — wired `etnyre-ghrist2000`.
2. `folio/quantum-observable-universe/fluid-dynamics/braid-fluid.ts` (`rem:braid-fluid`) — wired `moffatt1969`, `birman-williams1983`, `ghys2007`, `garside1969`, `dehornoy2015`.
3. `folio/quantum-observable-universe/brings-surface/mi-sw-abelianisation.ts` (`prop:mi-sw-abelianisation`) — wired `gaiotto-moore-neitzke2013`, `yekutieli2015`, `bralic1980`, `weber2005`, `riera-rodriguez-1992` (alongside upgraded `arxiv-1204.4824v2`).
4. `folio/quantum-observable-universe/appendix-mass-binding-algorithms/fivetwo-stokes-unimodular.ts` (`prop:fivetwo-stokes-unimodular`) — wired `faddeev_kashaev1994`, `andersen-kashaev2014`, `dimofte-gaiotto-gukov2013`, `dimofte-gaiotto-gukov2014`, `gueritaud2006`, `agol2011`, `porti1997`, `dubois2005`, `ohtsuki-takata-2015`, `garoufalidis-zagier2023`, `garoufalidis-zagier-2024`.
