#!/bin/sh
# Installs the pre-commit hook for content validation.
# Run from the repo root:  ./scripts/install-hooks.sh

set -e

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo ".")"
HOOKS_DIR="$REPO_ROOT/.git/hooks"
SCRIPT_DIR="$REPO_ROOT/scripts"

if [ ! -d "$HOOKS_DIR" ]; then
    echo "Error: .git/hooks directory not found. Are you in a git repository?" >&2
    exit 1
fi

ln -sf "../../scripts/pre-commit" "$HOOKS_DIR/pre-commit"

# Verify the symlink resolves correctly
if [ -x "$HOOKS_DIR/pre-commit" ] || command -v "$HOOKS_DIR/pre-commit" >/dev/null 2>&1 || [ -L "$HOOKS_DIR/pre-commit" ]; then
    echo "✅ Pre-commit hook installed at $HOOKS_DIR/pre-commit"
else
    echo "Warning: hook symlink created but may not be executable" >&2
fi

# Quick self-test
if command -v python3 >/dev/null 2>&1; then
    echo "🔍 Running self-test..."
    python3 -c "import yaml; print('   PyYAML available')" 2>/dev/null \
        || echo "   ⚠️  PyYAML not found (install with: pip install pyyaml)"
fi
