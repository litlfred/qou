---
name: simulator
roles: [collaborator, owner]
---

# Simulator Skill

## Role

Create, configure, and manage interactive simulator content objects.
Simulators are standalone HTML visualisations integrated into the paper
via the content-object framework, with parameterised views for snapshot
generation and interactive exploration.

## Content-object triple

Each simulator is a content object with three files:

```
content/<paper>/<chapter>/
  <simulator-name>.ts    — manifest (kind, params, views, html ref)
  <simulator-name>.md    — documentation (explains simulator + default view)
  <simulator-name>.html  — NOT here; lives at repo root (served as static file)
```

The `.html` file is a standalone single-page app served at the repo root
(e.g. `q_double_slit.html`). The `.ts` manifest references it via the
`html` field.

## Type system

### SimulatorBlock

```typescript
interface SimulatorBlock extends BlockBase {
  kind: "simulator";
  label: string;       // prefix: "sim:"
  html: string;        // path to HTML file (relative to repo root)
  defaultView: SimulatorView;
  views?: SimulatorView[];
}
```

### SimulatorView

```typescript
interface SimulatorView {
  name: string;        // e.g. "default", "bach-2013"
  title?: string;      // display title
  params: Record<string, number | string | boolean>;
}
```

### SimulatorRef (on other blocks)

Any block can reference a simulator via the optional `simulator` field:

```typescript
interface SimulatorRef {
  ref: string;    // label of the simulator (e.g. "sim:q-double-slit")
  view?: string;  // named view to activate (default: "default")
}
```

Multiple blocks can reference the same simulator with different views.

## Label convention

| Block kind | Label prefix | Example |
|-----------|-------------|---------|
| `simulator` | `sim:` | `sim:q-double-slit` |

## Builder function

```typescript
import { simulator } from "../../schema/builders";

export default simulator({
  label: "sim:q-double-slit",
  title: "q-Deformed Double-Slit Simulator",
  html: "q_double_slit.html",
  uses: ["def:substrate-parameter", "prop:local-substrate-q"],
  tags: ["double-slit", "q-deformation", "simulation"],
  defaultView: {
    name: "default",
    title: "Default: moderate q-deformation",
    params: { q: 1.1097, D: 0.5, d: 100, lambda: 500 },
  },
  views: [
    {
      name: "classical",
      title: "Classical limit (q = 1)",
      params: { q: 1.0, D: 0.5, d: 100, lambda: 500 },
    },
  ],
});
```

## Attaching simulators to blocks

Add a `simulator` field to any remark, example, definition, etc.:

```typescript
export default remark({
  label: "rem:q-deformed-double-slit",
  title: "Macroscopic scattering and the q-deformed double slit",
  simulator: { ref: "sim:q-double-slit" },
  // Or with a specific view:
  // simulator: { ref: "sim:q-double-slit", view: "bach-2013" },
});
```

The viewer renders a `[simulate]` button in the block header.

## Viewer integration

- **[simulate] button**: Appears in block header actions for any block
  with a `simulator` ref. Opens the simulator overlay.
- **Simulator overlay**: Full-screen iframe (below the control bar)
  loading the HTML simulator with view params as URL query params.
- **View selector**: Dropdown in the overlay header to switch between
  named views without closing the overlay.
- **Hash route**: `#/simulate/sim:q-double-slit` or
  `#/simulate/sim:q-double-slit/bach-2013` deep-links to a simulator.

## LaTeX rendering

Simulators render as `\begin{remark}` environments in LaTeX. If a
`rendered[]` snapshot is available, it is included as
`\includegraphics`. The `.md` documentation is rendered as the
environment body.

## Parameter passing

Parameters are passed to the simulator HTML via URL query string.
Simulator HTML files should read `URLSearchParams` on load:

```javascript
const params = new URLSearchParams(location.search);
const q = parseFloat(params.get('q') || '1.0');
```

## Existing simulators

| Label | HTML file | Description |
|-------|----------|-------------|
| `sim:q-double-slit` | `q_double_slit.html` | Overhead particle diffraction |
| `sim:double-slit-analytical` | `double_slit_simulator.html` | Analytical intensity plotter |
| `sim:brings-surface` | `brings_surface.html` | 3D spectral resolvent |
| `sim:quantum-brings-surface` | `quantum_brings_surface.html` | Chiral tubes + multi-canvas |

## Workflow: Adding a new simulator

1. Create the standalone `.html` simulator at the repo root
2. Create `.ts` manifest with `simulator()` builder in the relevant chapter
3. Create `.md` documentation explaining the simulator and its default view
4. Add the simulator block name to the chapter manifest's section blocks
5. Attach `simulator: { ref: "sim:..." }` to relevant remark/example blocks
6. Optionally add `rendered[]` snapshot for the LaTeX PDF

## Constraint rules

- `simulator-html-exists`: simulators must have an `html` field
- `simulator-ref-resolve`: blocks with `simulator.ref` must reference
  an existing simulator label in the document
- `md-exists`: simulators must have a companion `.md` file
- `uses-resolve`: standard cross-ref validation applies
