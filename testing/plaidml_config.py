# Copyright Vertex.AI

import os
import plaidml.settings

def config():
    filename = os.getenv('PLAIDML_CONFIG_FILE', '../vertexai_plaidml/plaidml/experimental.json')
    with open(filename) as file_:
        return file_.read()


def very_large_values_config():
    return """
{
  "platform": {
    "@type": "type.vertex.ai/vertexai.tile.local_machine.proto.Platform",
    "hals": [
      {
        "@type": "type.vertex.ai/vertexai.tile.hal.opencl.proto.Driver",
      }
    ],
    "hardware_configs": [
      {
        "sel": {
          "value": "true"
        },
        "settings": {
          "max_mem": 1000000,
          "max_regs": 1000000,
          "mem_width": 1000000,
          "threads": 10000,
          "vec_size": 100000
        }
      }
    ]
  }
}
"""
