**Conjecture (Leading-order $N_v$).**
*The electroweak topological invariant $N_v$ admits the leading-order closed form*

$$
  N_v \;=\; |S_5| \cdot q_0^{90}
        \;=\; 120 \cdot q_0^{90}.
$$

*The corresponding electroweak scale prediction is $v = 244.79 \;\mathrm{GeV}$, matching CODATA to $-0.58\%$.*

## Derivation sketch, conditional on the two conjectures in `uses[]`

*Assume (i) the Markov-trace-residual rescaling factor is $|S_5| = 120$, which is the content of [S_5 action on H_n(q) at the electroweak slice](n-v-bring-action.md), and (ii) the depth is $90$ generations, which is the content of [Brane-tower depth from m_e to v equals 90](n-v-tower-depth-ninety.md). Combining these yields the bridge identity $v/m_e = 40 \cdot q_0^{90}$. Substituting into $N_v = 3v/m_e$ gives $N_v = 120 \cdot q_0^{90}$.*

*The step from (i) and (ii) to the displayed form is arithmetic and holds as stated. **Neither premise is established**: both are conjectures this block declares in its own `uses[]`, and the depth-$90$ input is tracked as open. The section is therefore a conditional derivation, not a proof, and carries no $\square$.*

## Sub-leading correction

The exact CODATA value implies $N_v = 120 \cdot q_0^{90.0558}$. The structural origin of this correction remains unresolved.

## Comparison to other strategies

The parameterization is optimal among non-circular closed forms.

Two separate claims about the prefactor $120$ should not be run together, because only one of them is a derivation. That it **minimizes the residual** is a statement about fit quality — selection against the measured value, and so not evidence for the framework under the repository's no-fitting discipline. That it **derives from the geometric substrate** is the assertion of [S_5 action on H_n(q) at the electroweak slice](n-v-bring-action.md), which is open. The residual-minimisation does not establish the substrate origin, and the substrate origin is not what the residual measures.
