/**
 * Bibliographic identity of this paper — title, authors, date — held ONCE.
 *
 * Two things describe this work: the paper manifest
 * (`quantum-observable-universe.ts`), and the self-citation `leitner2026` in
 * `folio/schema/references.ts` that Lean `-- Ref:` comments and `cites[]` use.
 * Until 2026-09-29 each carried its own copy, and they had drifted — the
 * citation read "Quantum Observable Universe" by "Leitner, Fred" while the
 * paper is "On the Mechanics of Quantum Observable Universes" by Frederick Carl
 * Leitner. Both now read this module (owner ruling 2026-09-26: "leitner2026
 * should be in folio/"; bean `qou-yqko`).
 *
 * Dependency-free on purpose. `references.ts` is loaded by scripts that have
 * no platform link, and importing the manifest itself would pull in the
 * platform builders and widen what every one of them needs.
 */
export const paperIdentity: {
  title: string;
  authors: string[];
  date: string;
} = {
  title: "On the Mechanics of Quantum Observable Universes",
  authors: ["Frederick Carl Leitner"],
  date: "2026-03-21",
};
