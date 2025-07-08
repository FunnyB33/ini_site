# 自分サイトを作る。

## 構成
**Frontend：**
- HTML5 / CSS3
- Tailwind CSS（ユーティリティファーストで高速開発）
- JavaScript（ES6+）
- GSAP（GreenSock Animation Platform）＋ScrollTriggerプラグイン
- Alpine.js（軽量なリアクティブUI制御用／必要に応じて）

**Backend：**
- Python 3.10+ / Flask
- Flask Blueprints（モジュール分割）
- SQLAlchemy ORM ＋ Alembic（マイグレーション）
- Flask-Login（セッション認証）
- Flask-RESTful（API設計）

**Design：**
- Figma（ワイヤーフレーム＆プロトタイプ作成）
- Tailwind UI コンポーネント（有料UIキット／オプション）
- Heroicons（アイコン素材）

**Content Management：**
- Markdown ベース ＋ Flask-FlatPages（記事データ管理）
- Flask-Admin（管理画面）
- （別案）Headless CMS：Netlify CMS or Strapi（Git連携で記事管理）

**Infra：**
- Docker ＆ Docker Compose（ローカル開発・本番コンテナ化）
- AWS ECS / Fargate（コンテナ実行基盤）
- Amazon RDS（PostgreSQL）
- Amazon S3 ＋ CloudFront（画像・静的ファイル配信）
- GitHub Actions（CI／CD）

**AI-agent：**
- OpenAI API（GPT-4）を利用した記事タイトル・タグ自動生成エージェント
- LangChain ラッパーで「新着記事提案ボット」や「コメント自動モデレーション」
---
**グローバルナビゲーションメニュー**

`Home | About | Projects | Blog | Hobbies | Training | Contact`

- ヘッダー：主要ページへのリンク＋ハンバーガーメニュー
- サイドバー（ブログ一覧やアーカイブページで）：カテゴリ／タグリスト／最新記事
- フッター：コピーライト、SNSリンク、プライバシー・規約へのリンク

---
| ページ名             | パス                     | 内容・ポイント                                          |
| ---------------- | ---------------------- | ------------------------------------------------ |
| Home             | `/`                    | - 最新記事プレビュー<br>- 各セクション（自己紹介／プロジェクト／趣味／筋トレ）へのリンク |
| About （自己紹介）     | `/about`               | - プロフィール／経歴<br>- 技術スタック・使用ツール<br>- SNS・GitHubリンク |
| Projects （開発公開）  | `/projects`            | - 作ったアプリ一覧（サムネ＋概要＋リンク）<br>- GitHubリポジトリへの導線      |
| Blog （開発ブログ）     | `/blog`                | - 技術記事一覧<br>- タグ・カテゴリ絞り込み<br>- RSSフィード対応         |
| Hobbies （趣味）     | `/hobbies`             | 以下２つのサブページをまとめるトップ                               |
| ├ Photography    | `/hobbies/photography` | - 撮影ギャラリー（Lightboxなど）<br>- 撮影エピソード               |
| └ Gaming         | `/hobbies/gaming`      | - ゲームレビュー・攻略<br>- スクリーンショットギャラリー                 |
| Training （筋トレ記録） | `/training`            | - ワークアウトログ（種目・重量・回数）<br>- グラフ表示（Chart.jsなど）      |
| Contact          | `/contact`             | - お問い合わせフォーム（名前・メール・内容）<br>- スパム対策（reCAPTCHA）    |
| Search           | `/search`              | - サイト内全文検索<br>- オートコンプリート対応                      |
| Archive          | `/archive`             | - 年月別／タグ別の過去記事一覧                                 |
| Terms            | `/terms`               | - 利用規約                                           |
| Privacy          | `/privacy`             | - プライバシーポリシー                                     |
| Sitemap (HTML)   | `/sitemap`             | - 人間用サイトマップ                                      |
| 404 Not Found    | `/404` (カスタム)          | - 見つからないときの案内ページ                                 |
