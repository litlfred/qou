Let $(\mathbf{C}, A, \tau)$ be a quantum universe over a Noetherian
ring $R$ ([quantum universe](#def\:quantum-universe)); let $q$ denote the substrate parameter.  Assume observability
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([quantum observable universe](#def\:quantum-observable-universe)).  Then the brane tower
$\{A_n\}_{n \geq 0}$ constructed via
([jet prolongation](#prop\:jet-prolongation)) satisfies the Yekutieli lifting
condition ([Yekutieli lifting condition](#def\:yekutieli-lifting-condition),
[Yekutieli lifting](#prop\:yekutieli-lifting)), and $(\mathbf{C}, A, \tau)$
is a quantum observable universe with the following structural properties:

1. *:refterm[Descent]{#descent} terminates.*  The geometric :refterm[descent]{#descent} tower has finite
   length, bounded by $\mathrm{Krulldim} Z(\mathrm{End}_{\mathbf{C}}(A))$.  Observability ensures each step
   is a strict reduction (the $G_q$-action is faithful, so fixed-point
   reduction strictly decreases dimension).
2. *First obstruction equals the Euler class.*  The Yekutieli
   obstruction $\kappa_0 \in H^2(\mathcal{S}, \mathcal{B})$ equals the
   Euler class of the Reeb bundle.  Under the trace map,
   $\kappa_0 \mapsto \chi(A) = \mathrm{tr}(\mathrm{id}_A) \in R$.
3. *Perpetual obstruction.*  If $\kappa_0$ is non-torsion in
   $H^2(\mathcal{S}, \mathcal{B})$, then $\kappa_n \neq 0$ for all
   $n \geq 0$.  The class $\kappa_0$ and the jet corrections at
   level $n$ live in complementary subgroups of
   $H^2(\mathcal{S}, \mathcal{B})$, so the corrections cannot cancel
   $\kappa_0$.
4. *Branch point formula.*  The geometric :refterm[descent]{#descent} from
   $\mathbb{P}(V)$ ([projective line object](#def\:projective-line-object)) to
   points has $B$ branch points with total ramification
   $R_{\mathrm{tot}} = 2d + \lvert\chi(A)\rvert$ (Riemann--Hurwitz),
   where $d$ is the degree of the covering.
5. *Terminal fiber data.*  At each branch point $p$, the QOU
   reduces to fiber data $(A, \tau, q(p))$ with the involution
   $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$
   ([fibre adjoint involution](#prop\:fiber-adjoint-involution)).

## Lean formalization

The companion Lean `qu_to_qou_exists` currently encodes an existence stub (`∃ q, True`) pending a faithful statement; the structural proof above is the intended content, deferred via `sorry` (`-- Ref: [manuscript]` §3, `[yekutieli2010]`).
