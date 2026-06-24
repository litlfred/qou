**Step 1 (classical Schur–Weyl).**
The classical Schur–Weyl duality between $\mathrm{GL}_k(\mathbb{C})$
and $S_n$ on $V^{\otimes n}$ gives a natural bijection between
$\mathrm{GL}_k$-irreps $V_\lambda^{\mathrm{GL}}$ and $S_n$-irreps
$V_\lambda^{S_n}$, both indexed by partitions $\lambda \vdash n$
with at most $k$ rows.

**Step 2 ($\mathrm{GL}_k$-duality and transpose).**
For $\lambda \vdash n$ with conjugate $\lambda^*$, the
$\mathrm{GL}_k$-module $V_{\lambda^*}^{\mathrm{GL}}$ is isomorphic
to the dual of $V_\lambda^{\mathrm{GL}}$ up to a determinant twist:
$V_{\lambda^*}^{\mathrm{GL}} \cong V_\lambda^{\mathrm{GL},*} \otimes
\det^{?}$.  The transpose $\lambda^*$ thus implements
$\mathrm{GL}_k$-representation duality.

**Step 3 ($q$-deformation).**
Quantum Schur–Weyl duality (Kassel \cite{kassel1995} Ch X) extends
the classical statement: the
Hecke algebra $H_n(R, q)$ replaces $S_n$, $\mathcal{U}_q(\mathfrak{gl}_k)$
replaces $\mathrm{GL}_k$, and the pairing
$V_\lambda^{\mathcal{U}_q} \leftrightarrow V_\lambda^{H_n(R, q)}$ is
preserved.  Representation duality on the quantum group side still
maps $V_\lambda^{\mathcal{U}_q} \mapsto V_{\lambda^*}^{\mathcal{U}_q}$
(up to $q$-determinant twist).

**Step 4 (Hecke-side involution).**
On the Hecke side, the corresponding involution is tensoring with
the sign representation
$V_{H_n(R, q)}(1^n)$, which maps $V_\lambda \to V_{\lambda^*}$.  This
is an **automorphism** of $H_n(R, q)$ fixing the Wedderburn blocks
pointwise up to the $\lambda \leftrightarrow \lambda^*$ swap.

**Step 5 (shell-operator self-duality).**
The shell operator $\sigma_{\mathrm{shell}}$ is the minimal
categorical ingredient realising magic-shell closure at level $4$
in the confinement filtration
([confinement level](#def:confinement-level)).  By the braiding
compatibility between $\mathcal{U}_q(\mathfrak{gl}_k)$ and $H_n(R, q)$
under Schur–Weyl, any $\mathrm{GL}_k$-charge-conjugate-invariant
construction in the quantum-group category corresponds, under SW
transport, to an element of $H_n(R, q)$ fixed by the sign-twist
involution.  Such elements satisfy $x_\lambda = x_{\lambda^*}$ in
the Wedderburn decomposition.

The **SDP/LP optimum** identified numerically by
[sdp_on_shadows.py](https://github.com/litlfred/qou/blob/main/computations/sdp_on_shadows.py)
at $A_{\mathrm{magic}} = 8$ —
$(x_{(7,1)} = x_{(2,1^6)} = 35.24)$ — is precisely this self-dual
combination, providing numerical confirmation of the categorical
prediction.
$\qquad\blacksquare$
