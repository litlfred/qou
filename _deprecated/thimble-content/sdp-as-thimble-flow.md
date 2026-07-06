**Reading.** The operator-selection LP
([proposition](#prop:operator-selection-lp)) and its SDP
refinement ([SDP](#prop:confinement-sdp)) admit a
Picard--Lefschetz interpretation that exposes their geometric
content without changing any algebraic statement.  The dictionary
is short:

See [Table](#tbl:sdp-as-thimble-flow-table-data).

Three points are worth highlighting.

**(a)  The dual is the geometry.**  The shadow prices
$u_\lambda$ appearing in the LP/SDP dual are not a bookkeeping
nicety: they are exactly the depths along the real part of the
Seiberg--Witten action at which each thimble enters the
decomposition.  The AGENTS.md-mandated *both-sides*
emission of LP duals (`y0_star`, `y_star`, `active_set`,
`primal_obj`, `dual_obj`, `duality_gap`) is, geometrically, the
emission of the *thimble depths*.  A primal-only solve loses the
geometric data --- which Wedderburn blocks (= thimbles) actually
saturate at the optimum.

**(b)  The active set is the most-receptive sub-braid.**
$\mathcal{S}^\ast$ identifies the channels into which the bound
state actually settles.  Geometrically it is the list of
thimbles whose Newton flow reaches the optimum.  These are what
[Chapter 12](#chap:particle-interactions) calls the
*"most-receptive sub-braids"*; the SDP dual is how to compute
that list.

**(c)  The flow is steepest descent, not random search.**  The
two encountering knots do not "search" the space of operators
--- they descend along the gradient of $\operatorname{Re}(S)$.
The discreteness of the resulting topology is enforced one step
later by Mostow rigidity
([proposition](#prop:mostow-confinement)).

This remark is exposition: it does not prove anything new.  Its
purpose is to make the geometric content of the SDP visible to a
reader who has internalised
[Chapter 9](#chap:archimedean-universe) but is meeting the
operator-selection LP for the first time.
