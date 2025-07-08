# 自分サイト開発プロジェクト

## プロジェクト概要
自己紹介、スキル、制作物、趣味などを発信するパーソナルポートフォリオサイトです。

## 1. サイト構造

```
/
├── /about/           # 自己紹介・プロフィール
├── /works/           # 制作実績一覧
│   └── /:work_id/    # 個別作品詳細
├── /blog/            # ブログ記事一覧
│   └── /:post_id/    # 個別記事
├── /hobbies/         # 趣味のページ
│   ├── /photography/ # 写真作品
│   └── /gaming/      # ゲーム実績
├── /training/        # トレーニング記録
├── /contact/         # お問い合わせ
└── /admin/           # 管理画面（ログイン要）
```

## 2. 技術スタック

### フロントエンド
- **コア**: HTML5, CSS3, JavaScript (ES6+)
- **フレームワーク**: React.js (Next.js)
- **スタイリング**: Tailwind CSS + CSS Modules
- **アニメーション**: GSAP + ScrollTrigger
- **状態管理**: Alpine.js（軽量なインタラクション用）
- **UIコンポーネント**: Tailwind UI, Heroicons

### バックエンド
- **フレームワーク**: Python 3.10+ / Flask
- **アーキテクチャ**: Flask Blueprints（モジュール分割）
- **データベース**: PostgreSQL + SQLAlchemy ORM
- **認証**: Flask-Login（セッション認証）
- **API**: Flask-RESTful
- **マイグレーション**: Alembic

### インフラ
- **ホスティング**: Vercel (Frontend) + Render (Backend)
- **CI/CD**: GitHub Actions
- **監視**: Sentry
- **CDN**: Cloudflare

## 3. 主要機能

### ユーザー向け
- レスポンシブデザイン
- ダークモード対応
- パフォーマンス最適化
- アクセシビリティ対応
- サイト内検索
- コメント機能（Utterances連携）

### 管理者向け
- マークダウンエディタ
- メディア管理
- アクセス解析
- バックアップ機能

## 4. 開発フロー

1. **環境構築**
   - Docker Composeによる開発環境
   - 自動フォーマット・リンター設定
   - コミットフックの設定

2. **開発**
   - 機能単位でのブランチ運用
   - コンポーネント駆動開発
   - StorybookによるUI開発

3. **テスト**
   - ユニットテスト
   - E2Eテスト
   - パフォーマンステスト

4. **デプロイ**
   - プレビュー環境への自動デプロイ
   - 本番環境へのマージ時デプロイ
   - ロールバック戦略

## 5. ロードマップ

### 短期目標
- [ ] プロトタイプの作成
- [ ] 認証機能の実装
- [ ] ブログ機能の実装

### 中期目標
- [ ] パフォーマンス最適化
- [ ] アクセシビリティ対応
- [ ] 多言語対応

### 長期目標
- [ ] PWA対応
- [ ] オフライン機能
- [ ] APIの一般公開

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
