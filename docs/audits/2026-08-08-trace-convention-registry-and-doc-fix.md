# Which statement was wrong, what writhe $0$ actually buys, and a guard (bean `qou-n1dj`)

Follow-on to
[`2026-08-08-borromean-trace-convention-forcing.md`](2026-08-08-borromean-trace-convention-forcing.md)
(bean `qou-3qrv`), which established the contradiction. This audit answers the
three questions it left open — *which* statement is wrong, *why* anyone believed
the writhe-$0$ claim, and *what stops a recurrence* — and lands the registry.

**Nothing is wired, no tier changed, no production numerical value altered.**

## 1. Headline

| question | answer |
|---|---|
| Which statement is wrong? | **The scope note in `mass-theory/h3-markov-wenzl-weights-context.md`** — on both of its claims. But correcting it does not remove the disagreement; it *sharpens* it (§2). |
| Is the mass trace defined categorically or algebraically? | **Algebraically**, and with $z$ **stipulated**, not derived (§2). This is evidence *against* the charitable "the author was thinking in $\mathrm{Rep}(\mathrm{SU}_q(2))$" reading. |
| What is the defensible version of the writhe-$0$ claim? | Writhe $0$ makes the $y_{(3)}$–$y_{(1^3)}$ **split** invisible — not $y_{(2,1)}$. The author had a true lemma about the *chirality* ambiguity and applied it to the *C-vs-D* ambiguity, which is a different ambiguity (§3). |
| Does $\beta_{\mathrm{Bor}}$ satisfy the defensible version? | Yes — and that is exactly why it does **not** rescue the claim (§3). |
| Is the "image lies in $\mathrm{TL}_3$" reading available? | No. Refuted, scope (b), named invariant (§3). |

## 2. The definition chain, and which statement is wrong

Tracing back from `canonical_mass.py`:

| step | file:line | what it says |
|---|---|---|
| facade | `computations/canonical_mass.py:47` `proton_neutron_mass_mev` | reads `m-p-substrate-identity-50dps.witness.json`; **no formula fallback** |
| producer | `computations/m_p_substrate_identity_50dps.py:124` `trM_borromean` | the Lean closed form $(4+h^2-3h^4-h^6)/(h^2+4)$; docstring already declares **convention D** and already flags the premise as unmet |
| dressing | same file, `:175` `F_Bor` | $\lvert\mathrm{tr}_M(\beta_{\mathrm{Bor}})\rvert\,[3]_q!/q^3$ |
| **definition of the mass trace** | `content/quantum-observable-universe/mass-endomorphism/categorical-mass-markov.md:13` (`prop:categorical-mass-markov`) | "*where $\int_A : A \to R$ is the **Jones–Markov trace**, functioning as the Frobenius integral on $A$*", with $A = \mathrm{H}_n(R,q)$ |
| **the value of $z$** | `content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md:5` (`rem:markov-axioms-primitive`) | axioms 1–3 with $z = 1/(q^{1/2}+q^{-1/2})$ |

**Algebraic, not categorical.** The defining block names a functional on the
**full Iwahori–Hecke algebra** $\mathrm{H}_n(R,q)$ — a Frobenius integral on the
algebra — with no fibre functor, no $\mathrm{Rep}(\mathrm{SU}_q(2))$, and no
Temperley–Lieb quotient anywhere. And $z$ is not left free with the framework
choosing later: it is **written down**. Axioms 1–2 with an unspecified
stabilisation parameter admit a one-parameter family; axiom 3 stipulates one
member of it, and that member is **convention C**.

So the corpus's definition chain says **C** for the mass trace, and production
says **D**. Consequences for the two candidate wrong statements:

- The scope note's *description of the definition* ("the full-Hecke Ocneanu
  Markov trace, with parameter $z = 1/(q^{1/2}+q^{-1/2})$") is **faithful to the
  corpus**. It is not the error.
- The scope note's *claim about the compute* — "the framework's **mass and
  binding computations** use" that trace — is **half wrong**. Binding genuinely
  is on C (`binding_canonical.py` → `closed_form_tau_M.py:132 markov_z`
  $= 1/(\sqrt q + 1/\sqrt q)$ + `y_lambda_wenzl_bridge_numeric`). **Mass is
  not**: production mass is D, with ~30 `F_Bor` consumers.
- The scope note's insensitivity claim is **flatly false** (§3).

**The uncomfortable part, stated plainly.** Correcting the doc does not resolve
anything. It converts a muddle into a clean, documented disagreement: *the
corpus defines the mass trace to be C, and production computes D, and D is the
one that matches CODATA to the precision the framework claims.* Per the task's
standing instruction and the bean's own framing, **the trace was not switched**
— a −197 ppm move across ~30 consumers is an owner decision, and "D is the value
that matches" is not an argument, it is the failure mode under test.

**One more circularity to retire.** `h3-markov-wenzl-weights-proof.md` §Step 3
derives $y_{(2,1)} = 1/[2]_q^2$ *by comparing against the Borromean closed form*
— a D object. It is a consistency computation internal to D and cannot be cited
as evidence for selecting D. A note saying so is now in the block. The
independent characterisation of D remains the Temperley–Lieb uniqueness argument,
whose premise is the open half.

## 3. Why anyone believed the writhe-$0$ claim

Nobody writes that by accident, and the true statement nearby is a *good* one.

**The lemma.** For any normalised Markov trace on $\mathrm{H}_3(q)$
($\sum_\lambda y_\lambda d_\lambda = 1$, $d = (1,2,1)$) and any $\beta \in B_3$
with writhe $0$ and $\pi(\beta) = \mathrm{id}$:

$$
  \mathrm{tr}_M(\beta) \;=\; 1 + y_{(2,1)}\bigl(\chi^{(2,1)}(\beta) - 2\bigr).
$$

Verified symbolically for **arbitrary** $(y_{(3)}, y_{(1^3)})$ subject to
normalisation, together with $\partial\,\mathrm{tr}_M/\partial y_{(1^3)} = 0$ at
fixed $y_{(2,1)}$, in
[`probe_writhe0_trace_insensitivity.py`](../../computations/probes/probe_writhe0_trace_insensitivity.py)
(PASS, all checks). Mechanism: $\chi^{(3)} = q^{w}$ and
$\chi^{(1^3)} = (-q^{-1})^{w}$ both equal $1$ at $w = 0$, so only the *sum*
$y_{(3)} + y_{(1^3)}$ enters — and normalisation already pins it to
$1 - 2y_{(2,1)}$.

**The defensible version of the claim, therefore:**

> On writhe-$0$, $\pi = \mathrm{id}$ braids the trace is insensitive to the
> **split** between $y_{(3)}$ and $y_{(1^3)}$ — i.e. to the chirality /
> transpose-pair asymmetry — but **not** to $y_{(2,1)}$.

That is a true and useful statement, and it is *exactly the subject of the same
content block's own "Non-uniformity of the weights — chirality of the Jones
trace" section*: the bar-involution argument would give $y_{(3)} = y_{(1^3)}$;
the block explains it fails. The lemma says that failure is invisible on
writhe-$0$ braids. **The author had the right lemma about the wrong ambiguity.**
The chirality ambiguity moves weight *between* $y_{(3)}$ and $y_{(1^3)}$; the
C-vs-D ambiguity moves $y_{(2,1)}$ as well:

| | $y_{(3)}$ | $y_{(2,1)}$ | $y_{(1^3)}$ |
|---|---|---|---|
| C | $0.4153958$ | $0.2809296$ | $0.0227449$ |
| D | $0.5054042$ | $0.2472979$ | $0$ |

$y^{D}_{(2,1)} = 1/[2]_q^2$ exactly; $y^{C}_{(2,1)}$ differs from it by
$0.0336317$. Since $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6 \neq 2$,
the entire gap is one product:

$$
  \mathrm{tr}^{D}_M - \mathrm{tr}^{C}_M
  \;=\;
  \bigl(y^{D}_{(2,1)} - y^{C}_{(2,1)}\bigr)\bigl(-3h^4 - h^6\bigr)
  \;=\; 1.9554\times10^{-4},
$$

exact as a rational function (the symbolic difference cancels to $0$);
$195.82$ ppm at the proton pin. $\beta_{\mathrm{Bor}}$ **does** satisfy the
defensible version of the claim — and that is precisely why the defensible
version does not rescue the false one.

**The `TL_3` reading is not available — scope (b).** The candidate "the traces
agree on braids whose image lies in $\mathrm{TL}_3$" fails on a proved
invariant: $\chi^{(1^3)}(\beta) = (-q^{-1})^{w(\beta)}$ is a **unit** in $R$ for
every braid word (checked at $w = 1, 0, -2$: $-1/q$, $1$, $q^2$). No braid image
has a vanishing three-row component, so no braid image lies in the
$\mathrm{TL}_3$ part. The invariant is the invertibility of the one-dimensional
characters. This also means the categorical charitable reading cannot be
recovered *from the braid side*: if the TL premise holds, it holds because of
where the fibre functor lands, not because of anything about
$\beta_{\mathrm{Bor}}$.

## 4. The guard

[`docs/coordination/trace-convention-registry.md`](../coordination/trace-convention-registry.md)
+ JSON twin + validator, mirroring the kernel-constraints-registry pattern.
Rules and what each would have caught:

| rule | check | the defect it closes |
|---|---|---|
| R3 | recompute each row's $\beta_{\mathrm{Bor}}$ value from the code it names, $10^{-15}$ relative | a registry/doc value drifting from the code |
| R4/R5 | every Borromean trace function must declare its convention in its own source (curated entry points + **discovery** over `computations/`) | "a production entry point traces a braid without declaring its convention" |
| R6 | each recorded doc claim's convention must equal the channel's convention for the stated layer | **the defect that occurred** |
| R7 | no excluded tracer may be listed as a convention | the `tr_M_atomic` mislabel and its false 6.7 % alarm |
| R8 | a channel whose definitional and production conventions differ must be `disputed` **and** carry an `open_item` | the disagreement being recorded silently |

Two design choices worth naming:

- **Channels carry `definitional_convention` *and* `production_convention`.**
  The whole defect was that these differed and nothing held them side by side.
  Now the mass channel's dispute is a machine-visible field, not something a
  reader must reconstruct from two files in different directories.
- **`--selftest` replays the historical defects.** Three `regression_cases` rows
  encode the original bad doc claim, the `tr_M_atomic` mislabel, and a
  silently-disputed channel; the validator fails if any is *not* caught. A guard
  that can rot without noticing is not a guard.

**Baseline:** `PASS`, 0 errors, **21 warnings** — 21 Borromean tracers outside
`production_files` that do not declare a convention. Real backlog, surfaced
rather than suppressed. Both recorded $\beta_{\mathrm{Bor}}$ values were
live-confirmed against the code at $3.4\times10^{-19}$ relative.

## 5. What changed, what did not

**Changed** (docs, docstrings, new files only):

- `mass-theory/h3-markov-wenzl-weights-context.md` — scope note rewritten per
  channel; false insensitivity claim replaced by the lemma + the exact gap;
  notation bullet corrected from "mass pipeline" to "binding pipeline"; a scope
  correction note added.
- `mass-theory/h3-markov-wenzl-weights-proof.md` — §Step 3 direction-of-argument
  note (the $y_{(2,1)}$ determination is internal to D).
- `braids-and-knots/markov-axioms-primitive.md` — $z$ is a stipulation selecting
  convention C, and despite the "Jones–Markov" name it is not the trace whose
  closure is the Jones polynomial.
- Convention declarations in `borromean_binding_recompute.py`,
  `closed_form_tau_M.py`, `markov/markov_trace_canonical.py` (docstrings only).
- New: the registry (md + json), the validator, and
  `probe_writhe0_trace_insensitivity.py`.

**Not changed:** any production numerical value; the trace any channel uses; any
witness; any tier. The `mass` channel dispute stays open under bean `qou-3qrv`.

**Verification** (CI is `workflow_dispatch`-only, so the agent's own checks are
the gate): validator `PASS` with `--selftest --lint-docs`; the new probe PASS
(0/12 checks failed); render-QA **grep battery** run by hand on all three edited
math-bearing `.md` (balanced `$`/`$$`/`{}`/`\bigl`-`\bigr`, no `\operatorname`,
no list-marker hijack inside `$$`, no bare align) — the **pipeline render was
not run** (`folio-assistant` requires `scripts/setup-folio-assistant.sh`), so
these edits are **not machine-validated for render**, per the AGENTS.md
render-QA gate. No Lean was added.

## 6. Follow-ups (not done here)

1. **Owner decision on the `mass` channel** (bean `qou-3qrv`): either establish
   the TL premise, in which case D is forced and the definition chain should be
   corrected to say so, or accept C and take the −197 ppm. Do not decide by
   match.
2. **Drain the 21 R5 warnings** — one docstring line each, after confirming
   which trace each function computes. Do not infer the convention from the
   value it returns; that is how a mislabel becomes canonical.
3. **Lean the writhe-$0$ lemma.** It is a clean, generic-base-ring statement
   (`{R : Type*} [CommRing R]`, no archimedean content) and would upgrade the
   registry's `writhe0_lemma.lean` field from `null`.
4. **Consider extending the registry to $n > 3$** — the same doc-vs-code
   exposure exists for the $\mathrm{H}_4$ and $A \geq 4$ traces, which this pass
   did not touch.
