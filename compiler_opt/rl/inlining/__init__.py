# coding=utf-8
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Implementation of the 'inlining for size' problem."""

import gin

from compiler_opt.rl import problem_configuration
from compiler_opt.rl.inlining import config
from compiler_opt.rl.inlining import inlining_runner


@gin.register(module='configs')
class InliningConfig(problem_configuration.ProblemConfiguration):
  """Expose the regalloc eviction components."""

  def get_runner(self, *args, **kwargs):
    return inlining_runner.InliningRunner(*args, **kwargs)

  def get_runner_ctor(self):
    return inlining_runner.InliningRunner

  def get_signature_spec(self):
    return config.get_inlining_signature_spec()

  def get_preprocessing_layer_creator(self):
    return config.get_observation_processing_layer_creator()
