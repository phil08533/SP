#!/usr/bin/env bash
# Read-only Linux readiness report for the Space Hippie engine trial.
# Does not install packages, change settings, write files, or contact the network.
set -u

section() { printf '\n=== %s ===\n' "$1"; }
have() { command -v "$1" >/dev/null 2>&1; }

section "Operating system"
if [[ -r /etc/os-release ]]; then
  grep -E '^(NAME|ID|VERSION_ID|VERSION_CODENAME)=' /etc/os-release || true
else
  echo "/etc/os-release unavailable"
fi
printf 'Kernel: '
uname -sr 2>/dev/null || true

section "CPU and memory"
if have lscpu; then
  lscpu 2>/dev/null | grep -E '^(Architecture|CPU\(s\)|Model name|Thread|Core|Socket)' || true
else
  printf 'Logical CPU count: '
  nproc 2>/dev/null || true
fi
if have free; then free -h 2>/dev/null || true; fi

section "Graphics devices"
if have lspci; then
  lspci -nn 2>/dev/null | grep -Ei 'VGA compatible controller|3D controller|Display controller' || echo "No graphics devices reported by lspci"
else
  echo "lspci not installed; skipping PCI graphics listing"
fi
if have nvidia-smi; then
  nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>&1 || true
else
  echo "nvidia-smi unavailable (GPU may be non-NVIDIA or driver utility not installed)"
fi

section "Disk space"
df -h / 2>/dev/null || true

section "Build tools"
for tool in clang++ g++ cmake ninja make git; do
  if have "$tool"; then
    printf '%s: ' "$tool"
    case "$tool" in
      clang++) clang++ --version 2>/dev/null | head -n 1 ;;
      g++) g++ --version 2>/dev/null | head -n 1 ;;
      cmake) cmake --version 2>/dev/null | head -n 1 ;;
      ninja) ninja --version 2>/dev/null | head -n 1 ;;
      make) make --version 2>/dev/null | head -n 1 ;;
      git) git --version 2>/dev/null | head -n 1 ;;
    esac
  else
    printf '%s: not found\n' "$tool"
  fi
done

section "Vulkan"
if have vulkaninfo; then
  if have timeout; then
    timeout 12s vulkaninfo --summary 2>&1 | head -n 45 || true
  else
    vulkaninfo --summary 2>&1 | head -n 45 || true
  fi
else
  echo "vulkaninfo not installed; Vulkan status not verified"
fi

section "Display session"
printf 'Session type: %s\n' "${XDG_SESSION_TYPE:-unknown}"
printf 'Desktop: %s\n' "${XDG_CURRENT_DESKTOP:-unknown}"

section "Notes"
echo "This is a read-only snapshot, not proof that either engine will run correctly."
echo "No package, driver, graphics, or system configuration was changed."
echo "Review the output before sharing it; remove any details you do not want to disclose."
