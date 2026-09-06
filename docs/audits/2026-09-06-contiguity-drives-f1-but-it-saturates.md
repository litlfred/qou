# Contiguity does drive `f₁/f₀` — but it **saturates** at ⅔, well short of the grouped word

**Tests the reading** #6905 offered as interpretation rather than measurement:
that *contiguity* is the common dependency behind the three grouped-specific
properties. That reading makes a prediction, so it is testable rather than
merely plausible. Beans `qou-brng` / `qou-pdg9` / `qou-hu1f`.

## The prediction, and the falsification criteria set in advance

If contiguity is the driver, partially-contiguous words should **interpolate**
between the two canonical regimes. Declared before running:

- `f₁/f₀` **not monotone** along a contiguity-increasing walk ⇒ reading refuted.
- any value **outside** the `[borromean, grouped]` interval ⇒ interpolation
  picture wrong outright.

## Measured

Contiguity := fraction of adjacent letter pairs sharing a generator index.
Greedy walk from the Borromean word, each step the single swap that most
increases contiguity. `pn` free word, `n = 6`, `P = 3`, exact `Fraction`.

    endpoint    contiguity   f₁/f₀
    borromean     0.1905      1/2   (+0.5)
    grouped       0.8571     37/2  (+18.5)

    walk step   contiguity   f₁/f₀
      0           0.1905      1/2   ( +0.5)
      1           0.3810      8     ( +8.0)
      2           0.5714     17     (+17.0)
      3           0.6667     37/2   (+18.5)
      4           0.7619     37/2   (+18.5)

    rises 3   falls 0   all inside the interval: True

**Both criteria pass: monotone non-decreasing, nothing outside the interval.**

## The refinement — it saturates, and that is the real content

`f₁/f₀` reaches `37/2` at contiguity **0.6667** and does not move again, while
the grouped word sits at **0.8571**. So the relationship is **not
proportional**: contiguity beyond roughly two-thirds buys nothing.

That is a sharper statement than "contiguity drives `f₁/f₀`", and it is the part
worth keeping. The plain reading — more contiguity, more `f₁/f₀` — is *wrong
above the threshold*; what the data supports is a rise to a ceiling.

## An independent cross-check that fell out

#6905 found, from the counts, that at least one 1-swap neighbour of the grouped
word **ties** `37/2` (`max(neighbours) = 37/2 = canonical`, canonical not being
in the neighbour list). Here a **different** word — lower contiguity than
grouped, not a neighbour of it — also reaches `37/2`.

Two independent routes to the same value, from two separately-written runs.
`37/2` is achieved by a set of words, not by the grouped word uniquely.

## Scope, and what is NOT established

- **Five points.** Three strict rises and two ties. Thin, and stated as thin.
- **Greedy, not exhaustive.** The walk terminated at contiguity 0.7619 because
  no single swap improved contiguity further — it is a local stop, and it never
  reaches the grouped word's 0.8571. So this is *a* path between the regimes,
  not *the* path.
- **"Monotone" here means non-decreasing** (the last two steps tie), not
  strictly increasing.
- **One nucleus** (`pn`, `n = 6`), one precision.
- **Correlation along one path is not causation.** Contiguity and `f₁/f₀` move
  together here; nothing shown rules out a third quantity driving both. The
  saturation is evidence *against* the simplest causal story, not for it.
- **Not a claim about the physics.** Scope-(a).

## What would sharpen it

The threshold. If the ceiling is genuinely at ⅔ rather than an artifact of this
word, it should reproduce at another nucleus and under a non-greedy path. That
is the measurement that would turn "saturates around 0.667" into a number worth
a name.
