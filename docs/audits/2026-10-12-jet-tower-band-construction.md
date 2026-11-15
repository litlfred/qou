# Jet-tower band construction: what the corpus fixes, and what each band gives on Bring's surface

**Date:** 2026-10-12. **Beans:** `qou-lx8f` (owner-directed), routes `qou-2a2o` / `qou-n2aa`.
**Scope:** read-only audit. No content block, `.lean` or bean file was edited. Line numbers are
at `HEAD = 83e76cb8a` (which already carries the scope note on `thm:qu-to-qou` items 2–3).
**Discipline:** the band is never chosen *because* it makes the obstruction non-zero. Every band
below is evaluated for what it gives, and the verdicts use the AGENTS.md (a)/(b) scope rule.

Taken as given from this session, not re-derived: (a) $H^2(\Sigma,\mathcal O^\times)=0$ on a compact
Riemann surface; (b) $w_2(T\Sigma_4)=\chi \bmod 2=0$, so Bring is spin; (c) $e=c_1$ is the image of
$H^1(\mathcal O^\times)$ in $H^2(\mathbb Z)$; (d) the group-level and Čech constant-coefficient
lifting criteria are proved sorry-free in
`QOU/MathlibExt/CentralExtensionObstruction.lean` (`exists_lift_iff_coboundary`, :145) and
`CechCentralExtensionObstruction.lean` (`exists_cocycle_lift_iff`, :134).

Throughout, "the Reeb $\mathrm U(1)$-bundle on $\Sigma_4$" is read as the unit tangent circle
bundle, whose Euler number is $\chi(\Sigma_4)=2-2g=-6$ (Poincaré–Hopf). That is the reading under
which the corpus writes $e=\chi=-6$ (`lifting-and-descent/qu-to-qou-proof.md:33`). The corpus
never constructs a Reeb bundle *on $\Sigma_4$* explicitly. This reading is an assumption.

---

## 0. Verdict table

| band $\mathcal B$ | extension it comes from | $H^2(\Sigma_4,\mathcal B)$ | $\kappa_0$ for the Reeb bundle | item 2 | item 3 |
|---|---|---|---|---|---|
| $\mathbb Z$ (constant) | $\mathbb Z\to C^\infty(\mathbb R)\to C^\infty(\mathrm U(1))$, or $\mathbb Z\to\mathcal O\to\mathcal O^\times$ | $\mathbb Z$ | $c_1=e=-6$, **honest** | holds, but the extension is **not a jet step** | hypothesis met; conclusion **ill-posed** (§3) |
| $\mu_n$, incl. $\mathbb Z/2$ | Kummer $\mu_n\to\mathbb G_m\xrightarrow{(\cdot)^n}\mathbb G_m$; $\mathrm{SU}(2)\to\mathrm{SO}(3)$ | $\mathbb Z/n$ | $-6 \bmod n$; $0$ for $n=2$ | fails as stated: $\kappa_0$ is $e \bmod n$, not $e$ | vacuous: all torsion |
| $\mathcal O^\times$, $\mathbb G_m$ | archimedean band (corpus) | $0$ | $0$ | fails | vacuous |
| jet kernel $\mathrm{Sym}^{n+1}T^*\otimes E$ | $J^{n+1}\to J^n$ | $0$ | $0$ | fails | vacuous |
| $Z(\mathrm{Aut}A_n)$ | Bring proof | **undetermined** | reduces to $\mu_2$ or $\mathcal O^\times$ rows | — | vacuous on either reduction |
| $HH^2$ | — | **not a band**: type mismatch | — | — | — |

So no reading makes item 3 meaningful on $\Sigma_4$. Exactly one reading makes item 2 true, $\mathcal B=\mathbb Z$. In that reading the extension is the universal-cover / exponential sequence, which jet prolongation does not produce. The integer $-6$ does appear in the jet tower, but as the **Atiyah class**. That is a degree-1 obstruction to *splitting* the jet sequence, not a degree-2 $\kappa_0$ (§2.4).

---

## 1. What is lifted, and what the kernel is, according to the definitions

### 1.1 The defining lines

- **Jet object.** `jet-prolongation.md:1–5`: $J^1(A):=A\otimes\Omega^1(A)$ with $\Omega^1(A)=\ker(m\colon A\otimes A\to A)$. This is an object of $\mathbf C$. The block says nothing about groups or gerbes.
- **Tower.** `recursive-brane-tower.md:1,7`: $A_{n+1}=J^1(A_n)$, and the maps are *inclusions* $A_n\hookrightarrow A_{n+1}$ "through the unit section". The Lean twin `recursive-brane-tower.lean` adds a retraction `descent` with `descent ∘ ascent = id` (`retraction` field). `descent-lemma.md:1–7` gives restrictions $r_n\colon A_n\to A_{n-1}$ and a **surjective** algebra map $\mathfrak d_n\colon\mathrm{End}(A_n)\to\mathrm{End}(A_{n-1})$.
- **Band.** `quantum-characteristic-classes.md:1`: "$A_n$ is an object in a gerbe $\mathfrak G_n$ banded by the sheaf of units $\mathcal B$". It does not say units *of what*. `yekutieli-archimedean-band.md:1` and `yekutieli-lifting.md:8` give $\mathcal B=\mathcal O_M^\times$. `brings-surface/brings-is-qou-proof.md:29` gives $\mathcal B=Z(\mathrm{Aut}(A_n))$. `qu-to-qou-su2.md:11` uses $\mathbb Z$. `kummer-tower.md:29` and `motivic-perpetual-obstruction.md:11` use $\mathbb G_m$.
- **Lifting triple.** `yekutieli-triple.md:3–5`: the objects are local trivialisations of $A_n$, the 1-morphisms are $g^{(n)}_{ij}\in\mathrm{Aut}_{\mathbf C}(A_n|_{U_{ij}})$, and the 2-morphisms are $a^{(n)}_{ij}\colon g^{(n)}_{ij}\Rightarrow g^{(n+1)}_{ij}$ "living in $\mathcal B$". This is the closest the corpus gets to a definition. It implies $\mathfrak G_n$ is the gerbe of local forms of $A_n$, with automorphism sheaf $\mathrm{Aut}(A_n)$. It also implies the kernel is $\ker(\mathrm{Aut}(A_{n+1})\to\mathrm{Aut}(A_n))$. **Neither is stated.**
- **Lean.** `quantum-characteristic-classes.lean`: `ObstructionSpace : Type*` with an arbitrary `AddCommGroup` field. The band is unconstrained at the type level.

### 1.2 What the definitions do not determine

Three data are missing. Each one would determine the band:

1. **The gerbes $\mathfrak G_n$.** What their objects and morphisms are. The natural guess is $\mathfrak G_n=$ the gerbe of local forms of $A_n$, i.e. $\mathrm{Tors}(\mathrm{Aut}A_n)$.
2. **The functor $F\colon\mathfrak G_{n+1}\to\mathfrak G_n$.** Yekutieli's central extension needs a weak epimorphism $F$ whose kernel is central (`library/arxiv-0801.0083v4/sections/sec-000-0-introduction.md:45–52`). The corpus supplies maps in the wrong direction ($A_n\hookrightarrow A_{n+1}$) and never says which map induces $F$. The candidates are $\mathfrak d_{n+1}$ or $r_{n+1}$.
3. **The site $\mathcal S$ and the regularity class.** Smooth, holomorphic, Zariski or étale. This decides whether a jet kernel is a fine sheaf, a coherent sheaf, or something else.

### 1.3 Two internal tensions that follow from the definitions alone

- **T1. If the tower supplies the lift, every $\kappa_n$ is trivial.** Suppose $F$ is induced by descent and $A_{n+1}=J^1(A_n)$ is a global object of $\mathfrak G_{n+1}$ with $F(A_{n+1})\cong A_n$. The jet object is constructed globally (`jet-prolongation.md:1`), and the Lean retraction supplies exactly this. Then Yekutieli's lifting theorem (`…/sec-003-4-obstruction-classes.md:401–413`, "Obstruction to lifting objects") gives $\mathrm{cl}^2_F(A_n)=1$. So **under the tower's own construction, $\kappa_n=0$ for all $n$, in every band.** Persistence then requires that $J^1(A_n)$ *not* be a lift of $A_n$. The corpus never says what else it would be.
- **T2. The "unit section" is not canonical.** $\Omega^1(A)=\ker m$ has no unit, so $A\to A\otimes\Omega^1(A)$ needs a choice. In the classical jet sequence $0\to T^*\!\otimes E\to J^1E\to E\to 0$, the canonical map is the projection $J^1E\to E$. An $\mathcal O$-linear section $E\to J^1E$ is the same as a connection. Holomorphically, one exists iff the Atiyah class $a(E)$ vanishes (§2.4). So `recursive-brane-tower.md:7` asserts as canonical a map whose obstruction, for $T\Sigma_4$, is non-zero.

A third point is a conflation. `quantum-characteristic-classes-exists-proof.md:4–7` says a central extension of gerbes is "classified by a class in $H^2(\mathcal S,\mathcal B)$; this class is $\kappa_n$". That is not Yekutieli's statement. His $\mathrm{cl}^2_F(j)$ is attached to an **object** $j$ of $\mathfrak G_n(X)$, not to the extension (`sec-000:69–74`). $H^2(\mathcal S,\mathcal B)$ classifies $\mathcal B$-gerbes, not extensions of a given gerbe by $\mathcal B$.

---

## 2. Standard-mathematics routes on $\Sigma_4$

### 2.1 $\mathbb Z\to\mathbb R\to\mathrm U(1)$: yes, $\kappa_0=e=-6$ honestly

Take the sheaves $0\to\underline{\mathbb Z}\to C^\infty(-,\mathbb R)\xrightarrow{\exp 2\pi i}C^\infty(-,\mathrm U(1))\to 0$. This is an exact sequence of abelian, hence central, sheaves of groups.

- **This is a genuine instance of the Yekutieli setting.** His Example 3.27 (`sec-002-3-extensions-of-gerbes.md:695–720`) turns *any* central extension of sheaves of groups $1\to\mathcal N\to\mathcal G\to\mathcal H\to1$ into a central extension of torsor gerbes $1\to\mathcal N\to\mathrm{Tors}\,\mathcal G\to\mathrm{Tors}\,\mathcal H\to1$.
- **The non-discreteness of $\mathbb R$ is irrelevant.** The band is the kernel $\mathcal N=\underline{\mathbb Z}$. $\mathbb R$ enters only as the middle sheaf $\mathcal G$.
- **The hypothesis of Yekutieli's Prop. `prop:9`(2) holds.** It needs "enough $\mathcal N$-acyclic coverings" (`sec-004-5-…:84,116`). Good covers provide them for a constant sheaf on a manifold (`sec-004-5-…:38–44`, Example "exa:12").
- **The obstruction is $c_1$.** The obstruction to lifting a $\mathrm U(1)$-torsor $P$ is the connecting map $\partial[P]\in H^2(\Sigma,\mathbb Z)$, which is $c_1(P)$. For the unit tangent bundle this is $e=\chi=-6$, with the Poincaré–Hopf sign convention. The holomorphic version $\mathbb Z\to\mathcal O\to\mathcal O^\times$ gives the same class.
- **Lean (d) does not cover this case.** The Čech file proves the criterion for a *constant* group $E$ over an index set. Here the middle term is a sheaf of functions, so this instance still rests on the standard theorem (Grothendieck/Giraud; Brylinski, *Loop spaces…*, Ch. 4; Murray's lifting bundle gerbes). Brylinski and Murray are **not held** in `library/`. They are cited only through `arxiv-0808.1923v3/sections/sec-009-…:124`.

**But the lift is uninformative.** $C^\infty(\mathbb R)$ is fine, so every $\mathbb R$-torsor is trivial. "$P$ lifts" therefore means "$P$ is trivial", and $\kappa_0=c_1(P)$ is just the Chern class restated. Nothing in this extension involves $J^1$, $\Omega^1(A)$ or the Frobenius–Hopf structure. There is also no next level: no extension of the $\mathbb R$-torsor gerbe is defined that would play the role of $\mathfrak G_2\to\mathfrak G_1$.

**Verdict on item 2:** it holds in this band as a **definition-level identification**. The obstruction *is* $c_1$ by the connecting map. It is not derived from jet prolongation. The Gysin-sequence argument at `qu-to-qou-proof.md:19–20` names a different connecting map, from the sphere-bundle Gysin sequence. That map computes $e$ but is not a lifting obstruction of a gerbe extension.

### 2.2 $\mu_n$ and $\mathbb Z/2$: Kummer and spin

- **Kummer.** $1\to\mu_n\to\mathbb G_m\xrightarrow{(\cdot)^n}\mathbb G_m\to1$ is central, an instance of Example 3.27. A line bundle $L$ lifts, i.e. has an $n$-th root, iff $\deg L\equiv0\pmod n$. The obstruction is $\deg L \bmod n\in H^2(\Sigma,\mu_n)\cong\mathbb Z/n$.
  - For $T\Sigma_4$ the obstruction is $-6\bmod n$, which vanishes iff $n\mid6$.
  - **This is an honest home for the divisibility statement at `kummer-tower.md:17–23`.** That statement is placed in $H^2(\mathcal S,\mathbb G_m)$ (`kummer-tower.md:29`), where everything vanishes on a curve: by (a) analytically, and by Tsen ($\mathrm{Br}=0$) étale.
- **$n=2$.** This case is $\mathrm U(1)\xrightarrow{z^2}\mathrm U(1)$, and equally $\mathrm{SU}(2)\to\mathrm{SO}(3)$ restricted to the frame bundle. The obstruction is $w_2=\chi\bmod2=0$, matching fact (b). The corpus's $\mathbb Z/2$-centre reading therefore gives $\kappa_0=0$ on $\Sigma_4$.
- **Item 3.** $\mathbb Z/n$ is all torsion, so the hypothesis "$\kappa_0$ non-torsion" never holds.

### 2.3 $\mathcal O^\times$, $\mathbb G_m$, and the jet-group kernel

- **$\mathcal O^\times$ and $\mathbb G_m$.** $H^2=0$ by (a) and Tsen, so $\kappa_n=0$ for all $n$.
- **The jet-group kernel.** Read $\mathfrak G_n$ as the gerbe of $n$-jets of $E$, with automorphism sheaf the jet gauge group. Then the kernel of $J^{n+1}\mathcal G\to J^n\mathcal G$ is the vector-group sheaf $\mathrm{Sym}^{n+1}T^*\otimes\mathrm{ad}E$.
  - It is abelian, and central only when $\mathrm{ad}$ is trivial, e.g. for a $\mathrm U(1)$ structure group.
  - It is an $\mathcal O$-module. Smoothly it is fine, so $H^{\ge1}=0$. Holomorphically it is coherent on a curve, so $H^2=0$ by Grothendieck vanishing.
  - **So $\kappa_n=0$ for every $n$.**
- **Yekutieli's own deformation-quantization instance gives the same answer.** It has bands $\hbar^p\mathcal O_X$ (`sec-005-6-pronilpotent-gerbes.md:525–540`). His non-trivial example needs a non-zero class in $H^2(X,\mathcal O_X)$ (`:398–399`), which is impossible on a curve.

### 2.4 Where $-6$ does enter jet prolongation: the Atiyah class (degree 1)

The first jet sequence of a holomorphic line bundle $L$ on $\Sigma$ is $0\to K\otimes L\to J^1L\to L\to0$. Its extension class is the Atiyah class $a(L)\in H^1(\Sigma,K)\cong H^2(\Sigma,\mathbb C)\cong\mathbb C$. This class equals $c_1(L)$ up to the factor $\pm2\pi i$ (Atiyah, *Complex analytic connections in fibre bundles*, Trans. AMS 85 (1957); Weil's criterion). For $L=T\Sigma_4$ it is non-zero, since $\deg=-6$.

So the integer $-6$ is visible to jet prolongation, as the obstruction to the unit section of T2. But it is:

- a **degree-1** class, of the type of Yekutieli's $\mathrm{cl}^1$ for lifting isomorphisms, or a torsor of connections;
- in a **$\mathbb C$-vector space**, not in $H^2(\mathcal S,\mathcal B)$;
- **zero in the smooth category**, which is the regime `archimedean-lifting-intro.md:1` declares ("smooth jet bundles").

This shifts the degree by one, the same shift as fact (c). The Atiyah class is not in the library (grep for "Atiyah class": only bibliography entries in `arxiv-0801.3233v4`, `arxiv-0707.2052v1` and `arxiv-1305.7175v4`).

**Open, and not settled here:** whether the higher jet sequences $J^{n+1}L\to J^nL$ carry non-vanishing extension classes at every $n$ on $\Sigma_4$. They live in $H^1(\Sigma,K^{n+1}L\otimes(J^nL)^\vee)$. This is the one route on which a "perpetual" statement could be posed honestly, but in degree 1 and with no complementary-subgroup structure.

### 2.5 $Z(\mathrm{Aut}A_n)$ and $HH^2$

- **$Z(\mathrm{Aut}A_n)$** (`brings-is-qou-proof.md:29`) is determined only once $\mathrm{Aut}A_n$ is.
  - If $\mathrm{Aut}$ is the $\mathrm{SU}(2)$ gauge sheaf, the centre is the constant $\mathbb Z/2$, giving §2.2 and $\kappa_0=0$.
  - If $\mathrm{Aut}$ contains central scalars, the centre contains $\mathcal O^\times$, giving §2.3 and $\kappa=0$.
  - This is also Yekutieli's "fake global objects" case, $1\to Z(\mathfrak G)\to\mathfrak G\to\mathfrak G/Z\to1$ (`sec-000:80–86`). It requires an already-given gerbe $\mathfrak G$, which is missing datum 1.
- **$HH^2$** classifies first-order deformations. The obstructions to extending a deformation lie in $HH^3$ (Gerstenhaber). Neither is $H^2(\mathcal S,\mathcal B)$ for a sheaf $\mathcal B$, so this reading is a **type mismatch**, not a band.

---

## 3. The complementary-subgroups argument (`qu-to-qou-proof.md:23–29`; `kummer-tower.md:25–29`)

The argument says $\kappa_0\in\mathrm{im}(H^2(\mathcal S,\underline R)\to H^2(\mathcal S,\mathcal B))$, the corrections $\delta_n\in\mathrm{im}(H^2(\mathcal S,\mathcal O)\to H^2(\mathcal S,\mathcal B))$, the two images are complementary, and $\kappa_n=\kappa_0+\delta_n$. On $\Sigma_4$ it fails on four independent counts:

1. **$\delta_n=0$ in every band.** $H^2(\Sigma,\mathcal O)=0$ for a curve (Dolbeault; smooth $\mathcal O$ is fine), so its image is $0$. The decomposition reduces to $\kappa_n=\kappa_0$. The "cannot cancel" argument is then idle: persistence is just the statement $\kappa_0\ne0$, and §2 settles that per band.
2. **For $\mathcal B=\mathbb Z$ and a *divisible* base ring $R$ (e.g. $\mathbb R$, $\mathbb C$, $\mathbb Q$), the image containing $\kappa_0$ is also $0$.** *(Scoped by the parent session: the proof's $\underline{R}$ is the theorem's Noetherian base ring. If $R=\mathbb Z$, the map $H^2(\underline{\mathbb Z})\to H^2(\underline{\mathbb Z})$ is the identity and this count does not apply; counts 1, 3 and 4 do not depend on $R$.)* A sheaf map $\underline{\mathbb R}\to\underline{\mathbb Z}$ (or $\mathcal O\to\underline{\mathbb Z}$) is zero, because $\mathrm{Hom}(\text{divisible group},\mathbb Z)=0$. So $\kappa_0=-6$ cannot lie in $\mathrm{im}\,H^2(\underline{\mathbb R})$. The proof's placement of $\kappa_0$ is wrong in the only band where $\kappa_0\ne0$. The natural map runs the other way, $H^2(\mathbb Z)\to H^2(\mathbb R)$.
3. **$H^2(\Sigma_4,\mathbb Z)\cong\mathbb Z$ is indecomposable.** Any two non-zero subgroups $a\mathbb Z$, $b\mathbb Z$ meet in $\mathrm{lcm}(a,b)\mathbb Z\ne0$. So "complementary" subgroups with $\kappa_0\ne0$ in one of them force the other to be $0$. The step is true only when there are no corrections.
4. **$\kappa_n$ is not defined once $\kappa_0\ne0$.** Yekutieli's class is attached to an object $j\in\mathfrak G_n(X)$. If $\kappa_0\ne0$, then $A_0$ has no lift, so there is no object at level 1 whose $\kappa_1$ could be non-zero. "Perpetual obstruction" as written ("$\kappa_n\ne0$ for all $n$") is therefore not well-formed. It would need $\kappa_n$ redefined, e.g. as the class of the level-$n$ gerbe itself, and no such definition exists.

The "jet corrections" are defined only as "$\delta_n$ … isolates the $n$-th iterated jet prolongation" (`fluid-dynamics/ns-obstruction-computation.md:40`). By count 1 they vanish on $\Sigma_4$ whatever they are, provided they lie in the image of $H^2(\mathcal O)$ as `ns-obstruction-tower.md:40–44` states.

---

## 4. Verdicts, with (a)/(b) scope

Each verdict below is about $\Sigma_4$ only.

- **$\mathcal O^\times$, $\mathbb G_m$, jet kernels ($\mathcal O$-modules): scope (b) on $\Sigma_4$.**
  - $\kappa_n=0$ for all $n$.
  - Invariants: (a); Tsen ($\mathrm{Br}$ of a curve over $\mathbb C$ is $0$); Grothendieck vanishing $H^2(\text{coherent})=0$ in complex dimension 1; fineness of smooth $\mathcal O$-modules.
  - Items 2 and 3 fail or are vacuous in these bands. This is an exclusion *of these bands on this surface*. It is not an exclusion of the tower.
- **$\mu_n$, $\mathbb Z/2$, constant-centre $Z(\mathrm{Aut})$: scope (b) for item 3.** Invariant: $H^2(\Sigma_4,\mu_n)=\mathbb Z/n$ is torsion, so the hypothesis is never met. For item 2 the class is $e\bmod n$, which is $0$ for $n=2$ (fact (b)) and not equal to $e\in\mathbb Z$.
- **$\mathbb Z$: item 2 is TRUE as an identification, scope (a) on its relevance.** $\kappa_0=c_1=-6$ is honest via §2.1. But no derivation connects that extension to $J^1$, and T1 shows the tower's own lift makes $\kappa_n$ trivial. Item 3 is **ill-posed**, by §3 count 4, and its complementary step fails, by §3 counts 2–3. Counts 2 (for divisible $R$ only) and 3 are scope (b) against the *argument*, with invariants $\mathrm{Hom}(\text{divisible},\mathbb Z)=0$ and the indecomposability of $\mathbb Z$. They are not against a perpetual phenomenon as such.
- **$HH^2$: not a band.** Type mismatch.
- **Atiyah route (§2.4): open and promising, but it changes the theorem.** The jet-native class carrying $-6$ is $a(T\Sigma_4)\in H^1(K)$, holomorphic only. Adopting it would restate item 2 in degree 1. That is an owner decision, not a fix.

## 5. Implications for `thm:qu-to-qou`

| | status |
|---|---|
| Band $\mathcal B$ | **asserted, never constructed**. Six-plus incompatible readings (§1.1). Missing data: $\mathfrak G_n$, $F$, site (§1.2). |
| $\kappa_n$ as obstruction of the jet step | **asserted**. Contradicted by T1 if the tower supplies $A_{n+1}$ over $A_n$. |
| Item 2 ($\kappa_0=e$) | **derived only for $\mathcal B=\mathbb Z$ with a non-jet extension.** False for $\mathcal O^\times$, $\mathbb G_m$, $\mu_n$ and jet kernels. |
| Item 3 (perpetual) | **not well-formed** for $\mathbb Z$; vacuous in every other band. The complementary-subgroup step is refuted on $\Sigma_4$ (§3). |
| Honest replacements | (i) the $\mathbb Z$-band restatement, "$c_1$ is the obstruction to an $\mathbb R$-lift", which is true and empty; (ii) the Kummer $\mu_n$ divisibility, which is true and gives a home to `kummer-tower`; (iii) the Atiyah class route, which is open. |

**Derived here:** T1, T2, the four counts in §3, and the per-band $H^2$ computations, all from standard theorems with the references cited.
**Asserted in the corpus and still unsupported:** the band, the functor $F$, and the "complementary images".
**Open:** whether the higher jet extension classes on $\Sigma_4$ are all non-zero (§2.4), and what $\mathfrak G_n$ is meant to be.
