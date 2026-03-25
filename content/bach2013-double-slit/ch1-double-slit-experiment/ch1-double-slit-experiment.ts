import { chapter, section } from "../../schema/builders";

/**
 * Chapter 1: Controlled Double-Slit Electron Diffraction
 *
 * Single-chapter experimental paper: setup, slit control results,
 * single-electron buildup, and digitized intensity profile.
 */
export default chapter({
  number: 1,
  title: "Controlled Double-Slit Electron Diffraction",
  label: "chap:bach-double-slit",
  sections: [
    section({
      title: "Introduction",
      label: "sec:bach-introduction",
      blocks: ["bach-introduction"],
    }),

    section({
      title: "Experimental setup",
      label: "sec:bach-setup",
      blocks: [
        "bach-apparatus",
        "bach-slit-parameters",
      ],
    }),

    section({
      title: "Results",
      label: "sec:bach-results",
      blocks: [
        "bach-mask-control",
        "bach-single-electron-buildup",
        "bach-intensity-profile",
      ],
    }),
  ],
});
