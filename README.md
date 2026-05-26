<div align="center">

# Gerenciador de cluster de inferência de IA

**Gerenciador de cluster de inferência de IA distribuída**

<p>
  <a href="https://github.com/SrSatriano/distributed-ai-inference-cluster"><img src="https://img.shields.io/badge/GitHub-distributed-ai-inference-cluster-24292e?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
</p>

<p>
  <img src="https://img.shields.io/badge/versão-1.0.0-0ea5e9?style=flat-square" alt="versão" />
  <img src="https://img.shields.io/badge/licença-MIT-22c55e?style=flat-square" alt="licença" />
  <img src="https://img.shields.io/badge/idioma-pt--BR-blue?style=flat-square" alt="idioma" />
  <img src="https://img.shields.io/badge/CI-GitHub_Actions-8b5cf6?style=flat-square" alt="ci" />
</p>

<p><strong>Gateway que balanceia requisições LLM entre workers CPU/GPU com observabilidade.</strong></p>

<p>
  Autor: <a href="https://github.com/SrSatriano">@SrSatriano</a> ·
  Release <strong>1.0.0</strong> (2026-03-26)
</p>

</div>

---

## Índice

1. [Visão geral](#visão-geral)
2. [Problema e solução](#problema-e-solução)
3. [Para quem é](#para-quem-é)
4. [Casos de uso](#casos-de-uso)
5. [Funcionalidades](#funcionalidades)
6. [Stack tecnológica](#stack-tecnológica)
7. [Arquitetura](#arquitetura)
8. [Estrutura do repositório](#estrutura-do-repositório)
9. [Pré-requisitos](#pré-requisitos)
10. [Instalação e execução](#instalação-e-execução)
11. [Configuração](#configuração)
12. [Testes](#testes)
13. [Performance](#performance)
14. [Deploy e operação](#deploy-e-operação)
15. [Limitações conhecidas](#limitações-conhecidas)
16. [Roadmap](#roadmap)
17. [Documentação complementar](#documentação-complementar)
18. [Segurança e licença](#segurança-e-licença)

---

## Visão geral

Este repositório faz parte do **portfólio de engenharia** mantido por [@SrSatriano](https://github.com/SrSatriano). A versão **1.0.0** entrega implementação do núcleo do produto, testes automatizados, pipeline de integração contínua e documentação operacional em **português brasileiro**.

O objetivo é permitir que você clone, execute e evolua o projeto com clareza — do desenvolvimento local ao deploy em produção.

## Problema e solução

| | |
|---|---|
| **Problema** | Um único servidor de inferência satura sob picos de tráfego. |
| **Solução** | Roteamento least-queue, health checks e HPA baseado em fila. |

## Para quem é

Engenheiros de ML ops e plataformas internas de IA.

## Casos de uso

- Chat interno corporativo
- Batch de embeddings

## Funcionalidades

- [x] Roteamento least-queue com health check
- [x] Manifests Kubernetes e HPA
- [x] Bootstrap de workers documentado
- [x] Dashboard Grafana
- [x] Roteamento sensível a temperatura GPU (opcional)

## Stack tecnológica

| Camada | Tecnologias |
|--------|-------------|
| **Principal** | Kubernetes, FastAPI, Prometheus, Grafana |

## Arquitetura

```mermaid
flowchart TB
  GW[API Gateway] --> LB[Balanceador]
  LB --> W1[Worker GPU]
  LB --> W2[Worker CPU]
  GW --> PROM[Prometheus]
  PROM --> GRAF[Grafana]
```

Detalhamento de componentes, fluxos de dados e decisões de design: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Estrutura do repositório

| Caminho | Descrição |
|---------|-----------|
| `k8s/` | Manifests |
| `api/` | Gateway FastAPI |

## Pré-requisitos

Cluster Kubernetes 1.28+ ou kind/minikube local.

## Instalação e execução

```bash
git clone https://github.com/SrSatriano/distributed-ai-inference-cluster.git
cd distributed-ai-inference-cluster
```

```bash
kubectl apply -f k8s/
uvicorn api.main:app --host 0.0.0.0 --port 8080
```

## Configuração

| Variável | Descrição | Exemplo |
|----------|-----------|--------|
| `WORKER_URLS` | Lista de workers | `http://worker1:8000,http://worker2:8000` |

> **Importante:** nunca faça commit de arquivos `.env` com segredos reais. Use `.env.example` como referência.

## Testes

Execute a suíte de testes antes de abrir pull requests:

```bash
pytest api/tests/ -q
```

A pipeline [`.github/workflows/ci.yml`](.github/workflows/ci.yml) repete build e testes em cada push para `main`.

## Performance

| Workers | Tokens/s agregados |
|---------|-------------------|
| 4× GPU | ~1,2k tok/s |

Metodologia, hardware de referência e flags de compilação: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Deploy e operação

| Guia | Conteúdo |
|------|----------|
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Homologação, produção e rollback |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Monitoramento, alertas e incidentes |

## Limitações conhecidas

- Requer GPUs provisionadas para carga real

## Roadmap

- Autoscaling por fila Redis

## Documentação complementar

| Documento | Descrição |
|-----------|-----------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Arquitetura e decisões técnicas |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deploy passo a passo |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Runbook operacional |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como contribuir |
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |
| [SECURITY.md](SECURITY.md) | Política de segurança |
| [AUTHORS.md](AUTHORS.md) | Créditos |

## Segurança e licença

- Dependências revisadas na release **1.0.0**
- Vulnerabilidades: siga [SECURITY.md](SECURITY.md)
- Licença: [MIT](LICENSE) © SrSatriano 2026

---

<p align="center">Desenvolvido com foco em clareza e engenharia de produção · <a href="https://github.com/SrSatriano/distributed-ai-inference-cluster">Ver no GitHub</a></p>
