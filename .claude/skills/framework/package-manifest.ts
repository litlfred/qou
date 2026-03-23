/**
 * Package Manifest — Docker and system dependency declarations.
 *
 * Each skill package declares its runtime requirements so the Docker
 * image builder can aggregate dependencies across all active packages.
 *
 * Uses OCI image spec annotations where applicable:
 *   https://github.com/opencontainers/image-spec/blob/main/annotations.md
 *
 * APT dependency format follows Debian control file conventions:
 *   https://www.debian.org/doc/debian-policy/ch-relationships.html
 */

/** An APT package dependency with optional version constraint. */
export interface AptDependency {
  /** Package name (e.g., "texlive-full", "ripgrep"). */
  package: string;
  /**
   * Version constraint using Debian relation syntax:
   * ">>1.0", ">=2.3", "=1.2.3-1", "<<3.0".
   * Omit for any version.
   */
  version?: string;
  /** Why this package is needed. */
  reason?: string;
}

/** A tool installed via curl/script rather than APT. */
export interface InstallerDependency {
  /** Tool identifier (e.g., "bun", "elan", "uv"). */
  name: string;
  /** Install command or URL. */
  installCommand: string;
  /** Expected binary on PATH after install. */
  binary: string;
  /** Pin to a specific version (empty = latest). */
  version?: string;
  reason?: string;
}

/** A Python package installed via pip/uv. */
export interface PythonDependency {
  /** PyPI package name. */
  package: string;
  /** PEP 440 version specifier (e.g., ">=1.0,<2.0"). */
  version?: string;
  reason?: string;
}

/** An npm/bun package dependency. */
export interface NodeDependency {
  /** npm package name. */
  package: string;
  /** semver range (e.g., "^1.0.0", ">=2.0.0"). */
  version?: string;
  reason?: string;
}

/**
 * Package manifest declaring all runtime requirements for a skill package.
 *
 * The Docker image build process reads these manifests to generate
 * an aggregate Dockerfile layer that satisfies all active packages.
 */
export interface PackageManifest {
  /** Package identifier matching skills-config.json name or "local". */
  packageId: string;

  /** Human-readable name. */
  name: string;

  /** What this package provides. */
  description: string;

  /**
   * Target OS. Ubuntu LTS releases only.
   * @default "ubuntu:24.04"
   */
  baseImage: string;

  /** Required CPU architecture(s). */
  architectures?: ("amd64" | "arm64")[];

  /**
   * OCI annotations for the resulting image layer.
   * @see https://github.com/opencontainers/image-spec/blob/main/annotations.md
   */
  ociAnnotations?: {
    "org.opencontainers.image.title"?: string;
    "org.opencontainers.image.description"?: string;
    "org.opencontainers.image.authors"?: string;
    "org.opencontainers.image.url"?: string;
    "org.opencontainers.image.source"?: string;
    "org.opencontainers.image.licenses"?: string;
    [key: string]: string | undefined;
  };

  /** APT packages (Ubuntu/Debian). */
  apt?: AptDependency[];

  /** Tools installed via custom scripts/curl. */
  installers?: InstallerDependency[];

  /** Python packages (installed via uv/pip). */
  python?: PythonDependency[];

  /** Node/Bun packages. */
  node?: NodeDependency[];

  /** Environment variables required at runtime. */
  envVars?: {
    name: string;
    description: string;
    required: boolean;
    default?: string;
  }[];

  /** Ports exposed by services in this package. */
  exposedPorts?: {
    port: number;
    protocol: "tcp" | "udp";
    service: string;
  }[];

  /** Healthcheck command (OCI-compatible). */
  healthcheck?: {
    test: string[];
    interval?: string;
    timeout?: string;
    retries?: number;
  };
}
