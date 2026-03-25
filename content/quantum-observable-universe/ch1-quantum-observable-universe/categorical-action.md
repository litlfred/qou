Let $(\mathcal{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
$q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)),
a connection $\nabla$ ([categorical connection](#def:categorical-connection)),
and a section $\psi \colon \mathbf{1} \to A$ (a "state").
The *categorical action* is the $R$-valued functional

$$
  \mathcal{S}_q[\nabla,\, \textstyle\int_A,\, \psi]
  \;=\;
  \underbrace{
    \mathrm{tr}\bigl(q \cdot R_{\int}\bigr)
  }_{\text{gravity}}
  \;+\;
  \underbrace{
    \int_A \!\circ\, \mathrm{tr}_A\bigl(
      F_\nabla \wedge_q \star_q F_\nabla
    \bigr)
  }_{\text{gauge}}
  \;+\;
  \underbrace{
    \int_A\!\bigl(\psi^* \cdot D_\nabla\,\psi\bigr)
  }_{\text{matter}},
$$

with notation as in [categorical action notation](#rem:categorical-action-notation).
