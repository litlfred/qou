import type { PackageManifest } from "./package-manifest.js";

/**
 * Template for skill packages to declare their Docker requirements.
 *
 * Copy this file into your skill package directory as `package-manifest.ts`
 * and fill in the requirements. The Docker image builder reads these
 * manifests to aggregate dependencies across all active packages.
 *
 * Example: a WHO SMART Guidelines authoring package would declare
 * FHIR tooling, IG Publisher, and SUSHI as its requirements.
 */
export const templateManifest: PackageManifest = {
  packageId: "your-package-id",
  name: "authoring-who-smart-guidelines",
  description: "WHO SMART Guidelines IG authoring assistant",
  baseImage: "ubuntu:24.04",
  architectures: ["amd64"],

  ociAnnotations: {
    "org.opencontainers.image.title": "Your Package Title",
    "org.opencontainers.image.description": "What this package does",
    "org.opencontainers.image.source": "https://github.com/org/repo",
    "org.opencontainers.image.licenses": "MIT",
  },

  apt: [
    { package: "ca-certificates", reason: "TLS" },
    { package: "curl", reason: "Downloads" },
    { package: "git", reason: "Repository operations" },
    // Add your APT dependencies here
    // { package: "default-jre", reason: "FHIR IG Publisher requires Java" },
    // { package: "nodejs", version: ">=18", reason: "SUSHI compiler" },
  ],

  installers: [
    // { name: "sushi", installCommand: "npm install -g fsh-sushi", binary: "sushi", reason: "FSH → FHIR compiler" },
    // { name: "ig-publisher", installCommand: "curl -L -o publisher.jar ...", binary: "java -jar publisher.jar", reason: "HL7 IG Publisher" },
  ],

  python: [],
  node: [],

  envVars: [
    // { name: "FHIR_SERVER_URL", description: "FHIR server for validation", required: false },
  ],

  exposedPorts: [],

  healthcheck: {
    test: ["CMD", "echo", "ok"],
    interval: "30s",
    timeout: "5s",
    retries: 3,
  },
};
