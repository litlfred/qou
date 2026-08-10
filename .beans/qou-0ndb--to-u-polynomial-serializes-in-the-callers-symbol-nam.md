
---

## The open call is answered: the two copies do NOT become one helper

PR #4926. The bean left this as "a separate call". Resolved: normalise the
**serialization step** in the probe copy, do not merge the functions.

`probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py` was serializing
three committed witness fields — `denom_in_u`, `p_in_u_factored`,
`diff_p_in_u` — with a bare `str()`. So the symbol name in those fields was
a property of one local variable (line 357), not of the format. It read `u`
only because that variable is spelled `u`: correct by luck, and one rename
from being wrong in exactly the way that cost this family four instances.

All three now route through `str_in_u`. That imports the canonical
SERIALIZER, not the canonical algorithm — the probe's local primitives stay
a deliberate mirror, which is what its own comment says they are for.

**Why not merge.** The defect never lived in the algorithm; the two copies
compute the same thing correctly. It lived entirely in the step that turns
an expression into text. Merging would collapse a deliberately
self-contained probe into a dependency on the module it mirrors to fix a
problem one line of that module already fixes. Normalising the one step
buys the invariant without the coupling.

**No witness regenerated, and none needed.** The probe's symbol is
`sp.Symbol("u", positive=True, real=True)`, which IS `U_CANONICAL`, so
`str_in_u` takes its identity fast path and returns exactly what `str()`
returned. Verified byte-identical on four representative expressions
including the zero case.

## The two-name `locals` workaround: retirement condition partly met

The bean's standing rule is that `locals={"u": u, "check_q": u}` must stay
until every affected witness is regenerated. Status after #4926:

* all 20 `_habiro_coefficient_extract.ATOMS` witnesses — regenerated;
* the 5 `extend_even_a_mirror_pair_test.EVEN_A_OPEN` witnesses — regenerated;
* `habiro-coefficients-atomic.witness.json` — **not** regenerated. Its
  `p_in_u` / `denom_in_u` still say `check_q`, and it is the upstream input
  every one of the above loads `τ_p` / `τ_n` from.

So the workaround **stays**. It is not yet a cleanup that can be done
safely, and the file that pins it is now identified rather than merely
suspected. Retiring it means regenerating the atomic witness first and
re-running everything downstream of it — a larger, separate arc.
