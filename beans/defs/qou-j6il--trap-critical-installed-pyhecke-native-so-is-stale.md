---
# qou-j6il
title: 'TRAP (critical): installed pyhecke_native .so is STALE and returns convention C -- any producer run silently reintroduces C'
status: completed
type: task
priority: normal
created_at: 2026-08-09T22:00:28Z
updated_at: 2026-08-10T00:48:34Z
---


## The trap

```
$ python3 -c "import pyhecke_native as p; print(p.markov_z(1.1099785827513808075916690956107688798744991218736))"
0.4993203341836945          <-- convention C
```

but the Rust source it is supposedly built from says convention **D**:

```rust
/// z = q³/(q² + 1) — Markov closure parameter, **trace convention D**
#[inline]
pub fn markov_z(q: f64) -> f64 {
    q * q * q / (q * q + 1.0)
}
```
`tools/hecke-engine/src/gram.rs:75`

**The installed binary is stale.**

| | |
|---|---|
| installed `.so` built | **2026-08-08 11:30:19 UTC** |
| `b5f4cb5b9` "qou-wgta item 10: the Rust engine stack C -> D, all nine bindings" | **2026-08-09 13:18:31 UTC** |

The wheel predates the migration by ~26 hours. Source is D; the artifact
executing is C.

## Why this is the worst kind of defect in this excision

Every other convention-C site found so far is *visible* — a formula or a number
in a file, catchable by grep or by the `trace-convention` axis. This one is
invisible to all of them: the source reads correctly, the registry reads
correctly, the axis passes, and the binary silently returns C.

Worse, it turns the standard remediation into a **reintroduction vector**. The
instruction throughout this excision has been "never hand-edit witness numbers,
regenerate from the producer". Doing exactly that, right now, with this binary
installed, would stamp fresh convention-C numbers into witnesses and content —
carrying the authority of a producer run and a `deps_hash`.

`markov_z` is not incidental. Its own docstring: *"re-exported through all nine
language bindings (pyhecke-native, wasm, node, c, jvm, r, julia, gap, octave) and
drives `trace_weights` and the `v_std` quark-volume channel"*. So anything
downstream of `trace_weights` in the native path is affected.

## Actions

- [x] Diagnosed: stale artifact, not a source defect
- [ ] Rebuild `pyhecke-native` from the D source (`maturin build --release`;
      cargo and maturin are both present in the container)
- [ ] Verify `markov_z(q0) == 0.612688037146465252`, not `0.4993203341836945`
- [ ] **Only then** run any producer
- [ ] Check the other eight bindings for stale build artifacts — the migration
      commit touched all nine, so if the Python wheel was stale the others
      plausibly are too. wasm/node are the ones most likely to be shipped
      pre-built.
- [ ] Consider a guard: a startup assertion, or a test, that fails when
      `markov_z(q0)` does not match the registry's `z_at_q0` for convention D.
      A stale binary should be loud, not silent.

## The general lesson

A compiled artifact is a convention surface, and it is the only one where source
review cannot see the defect. The `trace-convention` axis walks `content/**`; the
registry validator walks `computations/`, `tools/`, `qou-mass/`. **Nothing checks
that a built artifact agrees with the source it claims to come from.** The guard
above is the cheap fix and it belongs in CI, not in a bean.

---

## RESOLVED — three layers, covering all three paths a wheel can arrive by

The container rebuild fixed *this* container and dies with it, so it was never
the fix. The question is which paths a `pyhecke_native` can reach a producer by,
and each now has a gate:

| path | guard | where | commit |
|---|---|---|---|
| **the image** | wheel is **built in-image** from the same tree as the engine, then gated | `litlfred/folio-assistant` `adapters/mcp-server/Dockerfile` | `561d833` |
| manual install | gate appended to the install script | `scripts/build-pyhecke-native.sh` | `550bf2d33` |
| already installed | R9 registry evaluator, fires whenever the validator runs | `trace-convention-registry.json` | `87f6e3ec8` |

**The image layer is the one that makes it structurally impossible rather than
detectable.** The Dockerfile already built the hecke-engine binaries from source
but never built the Python wheel *at all* — so whatever wheel a container ended
up with came from outside the image and could drift arbitrarily from the engine
shipped beside it. Now both artifacts come out of the same stage, from the same
source. They cannot disagree.

Built `--no-default-features`: that drops `clarabel-lp` (the litlfred
Clarabel.rs fork, unreachable from restricted-network builders), which the Gram /
seminormal / Markov-trace primitives do not need — only `operator_selection_lp`
does.

The install and gate are deliberately **not** failure-tolerated, unlike the
`lake` steps beside them. A missing `pyhecke_native` degrades gracefully
(producers have Python fallbacks); one carrying the wrong convention does not —
it emits numbers indistinguishable from ordinary producer output.

All three read `z_at_q0` from the registry rather than a literal, so changing the
production convention re-arms them instead of grandfathering the old value.

### Proven to fire, not just to pass

A gate that cannot fail is worth nothing, so both failure modes were tested:

```
stale convention-C wheel : markov_z(q0)=0.4993203341836945  |d|=1.134e-01
   -> FATAL: wheel is CONVENTION C            build fails  ✓
neither convention       : markov_z(q0)=0.5               |d|=1.127e-01
   -> FATAL: matches neither convention       build fails  ✓
correct wheel            : |d|=0.000e+00      convention D confirmed  ✓
```

The two failure modes are distinguished rather than collapsed, because they need
different responses: "stale, rebuild" versus "this is not either convention".

- [x] Diagnosed: stale artifact, not a source defect
- [x] Rebuilt and verified `markov_z(q0) = 0.612688037146465252`
- [x] R9 registry evaluator for the compiled artifact
- [x] Gate in the install script
- [x] Gate in the image, wheel built in-image
- [x] Other eight bindings checked — all live Rust is D; the sole C occurrence,
      `hecke-engine/src/archive/v2.rs:205`, is in no module tree (`mod archive`
      appears nowhere) and never compiles
- [ ] Still open: the atom-table producer does not exist and must be written
      before `prf:interface-knot-markov-z` can be regenerated

### What generalises

A compiled artifact is a convention surface, and the only one where source review
cannot see the defect. The pattern worth reusing: **build the artifact and its
consumer from one source in one stage, and gate the built artifact against the
registry rather than against a literal.** Detection alone was not enough here —
the whole point is that the detector would only have run if someone thought to
run it.
