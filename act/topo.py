import logging

import toposort

from act import logger

LOG = logging.getLogger(__name__)


def get_all_deps(node, d):
    deps = []

    def inner(node, d):
        exists = d.get(node)
        if exists:
            needs = exists.get("needs")
            if needs:
                for i in needs:
                    deps.append(i)
                    inner(i, d)

    inner(node, d)

    return set(deps)


def _topify(d):
    try:
        return list(toposort.toposort(d))
    except toposort.CircularDependencyError as e:
        msg = f"Failed to build graph.\n\n'{e}'"
        logger.sysexit_with_message(msg)


def get_topo_for(node, d):
    deps = get_all_deps(node, d)

    return _topify({node: deps})


def get_topo(d):
    d = {k: v.get("needs", {}) for k, v in d.items()}

    return _topify(d)
