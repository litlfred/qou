import { chapter, section } from "../../schema/builders";

/**
 * Authors' note — front matter following the Introduction (owner request
 * 2026-11-23, issue #9193). Moved out of the Introduction's last section and
 * expanded: verification and source, authoring method, compute
 * infrastructure, contribution policy and authorship.
 */
export default chapter({
  title: "Authors' Note",
  label: "chap:authors-note",
  sections: [
    section({
      title: "Verification and source",
      label: "sec:authors-note-verification",
      blocks: ["authors-note-verification"],
    }),
    section({
      title: "Authoring method",
      label: "sec:authors-note-authoring",
      blocks: ["authors-note-authoring"],
    }),
    section({
      title: "Compute infrastructure",
      label: "sec:authors-note-compute",
      blocks: ["authors-note-compute"],
    }),
    section({
      title: "Contributions and authorship",
      label: "sec:authors-note-contributions",
      blocks: ["authors-note-contributions"],
    }),
  ],
});
