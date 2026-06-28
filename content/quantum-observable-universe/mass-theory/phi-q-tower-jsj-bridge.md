> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The Φ$_q$–JSJ archimedean bridge is stated as
[`conj:phi-q-tower-jsj-bridge`](#conj:phi-q-tower-jsj-bridge): under
the archimedean realisation $\tau_{\mathrm{arch}}$, each dilogarithm
summand of the mass-endomorphism tower equals $\rho_q$ times the
hyperbolic volume of the corresponding Φ$_q$-piece, so that the
descended sum reproduces the JSJ piecewise volume
$\sum_{P \in \mathrm{JSJ}(K)} \rho_F(P) \cdot \mathrm{Vol}_{\mathrm{hyp}}(P)$
that drives the canonical binding-energy pipeline. The remark below
interprets that conjecture against the unconditional algebraic
stratification [`prop:phi-q-tower-algebraic-stratification`](#prop:phi-q-tower-algebraic-stratification),
which is what the bridge crosses the Archimedean wall to realise.

### Significance (rather than deprecating Φ$_q$)

The conjecture says the **dilog form** and the **hyperbolic-volume
form** of the tower are not two competing engines: they are two
presentations of the same archimedean number, evaluated through two
different convergence schemes.

- **JSJ pipeline.** For each piece $P$, evaluate
  $\mathrm{Vol}_{\mathrm{hyp}}(P)$ numerically with SnapPy. Fast on
  finished hyperbolic atoms; opaque internally.
- **Φ$_q$ pipeline.** For each $S$, evaluate
  $\Phi_q(\|V_S\|_F)$ as a Laurent polynomial in $q^{1/2}$.
  Slower convergence (the Kashaev limit is logarithmic), but yields a
  closed-form, $q$-differentiable expression per generator and per
  pair.

The bridge predicts that the two engines compute the same atomic-mass
target, and explains the empirical 0.15% Φ$_q$ floor on $D$ as a
**Kashaev-convergence floor**, not a model floor. Phase 2 of the
1ppb handover (pentagon-defect expansion) is intrinsically a
Φ$_q$ computation — the pentagon identity is the Φ$_q$ five-term
relation — so the dilog form earns its keep as a *theoretical* tool
while JSJ remains the numerical workhorse.

### Motivic dictionary

The bridge admits a clean motivic reading: the algebraic side
$\Phi_q(\|V_S\|_F)$ is a class in the quantum Bloch group
$\mathfrak{B}(q)$ ([quantum Bloch group](#def:quantum-bloch-group)), the
archimedean realisation $\tau_{\mathrm{arch}}$ is the $q$-deformed
Borel/Beilinson regulator, and the right-hand side is the standard
Neumann–Zagier decomposition of the volume of $S^3 \setminus K$ along
its hyperbolic pieces [`neumann-zagier1985`, `zagier1986`]. In this
language the conjecture is the statement that

- the quantum Bloch class $[\Phi_q(\lvert V_S\rvert)]$ regulates
  archimedeanly to the volume of the corresponding Φ$_q$-piece, and
- the Φ$_q$ stratification $\{K_S\}_S$ realises the JSJ stratification
  with regulator weights matching $\rho_F$.

The $\rho_q$ prefactor on the right-hand side is the substrate-density
normalisation that converts a regulator output (a real number) into a
mass density on the brane. Phrased this way, the dilog form and the
hyperbolic-volume form are not two competing engines but two
presentations of the same regulator, evaluated through two
convergence schemes.
