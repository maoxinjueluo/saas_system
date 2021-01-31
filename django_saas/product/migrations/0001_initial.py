# Generated by Django 2.0 on 2021-01-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
                ('store_category_id', models.PositiveIntegerField()),
                ('goods_id', models.PositiveIntegerField()),
                ('comment_data', models.TextField(blank=True, null=True)),
                ('image_src', models.CharField(max_length=1000)),
                ('is_hide', models.IntegerField()),
                ('star_rating', models.PositiveIntegerField()),
                ('comment_tag', models.CharField(max_length=255)),
                ('is_checked', models.IntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('star_rating', models.PositiveIntegerField()),
                ('tag_data', models.CharField(max_length=30)),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'comment_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('type', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=20)),
                ('is_show', models.PositiveIntegerField()),
                ('app_show', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsConsume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('category_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('image_src', models.CharField(max_length=1000)),
                ('describe', models.CharField(max_length=255)),
                ('bar_code', models.CharField(max_length=30)),
                ('unit_id', models.PositiveIntegerField()),
                ('specs', models.CharField(max_length=20)),
                ('type', models.PositiveIntegerField()),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quality_day', models.PositiveSmallIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_consume',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsConsumeBottleUnitConver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('consume_id', models.PositiveIntegerField()),
                ('unit_id', models.PositiveIntegerField()),
                ('min_conver_number', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_consume_bottle_unit_conver',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsConsumeUnitConvert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('consume_id', models.PositiveIntegerField()),
                ('unit_id', models.PositiveIntegerField()),
                ('conver_number', models.PositiveIntegerField()),
                ('is_min', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_consume_unit_convert',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsInvestCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('image_src', models.CharField(max_length=1000)),
                ('type', models.PositiveIntegerField()),
                ('money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('give_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('give_expire_type', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_invest_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('category_id', models.PositiveIntegerField()),
                ('describe', models.CharField(max_length=255)),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_src', models.CharField(max_length=100)),
                ('option_count', models.PositiveIntegerField()),
                ('type', models.PositiveIntegerField()),
                ('services', models.TextField(blank=True, null=True)),
                ('effective_day', models.PositiveIntegerField()),
                ('effective_type', models.IntegerField()),
                ('sort', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_package',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsPackageNotStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('category_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=255)),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_src', models.CharField(max_length=1000)),
                ('option_count', models.PositiveIntegerField()),
                ('type', models.PositiveIntegerField()),
                ('services', models.TextField(blank=True, null=True)),
                ('effective_type', models.IntegerField()),
                ('effective_day', models.PositiveIntegerField()),
                ('sort', models.PositiveIntegerField()),
                ('create_staff_id', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_package_not_standard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('category_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('bar_code', models.CharField(max_length=30)),
                ('unit_id', models.PositiveIntegerField()),
                ('specs', models.CharField(max_length=20)),
                ('image_src', models.CharField(max_length=1000)),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.PositiveIntegerField()),
                ('quality_day', models.PositiveSmallIntegerField()),
                ('content', models.TextField(blank=True, null=True)),
                ('all_store_display', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsProductDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_product_display',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsProductUnitConvert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField()),
                ('unit_id', models.PositiveIntegerField()),
                ('conver_number', models.PositiveIntegerField()),
                ('is_min', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_product_unit_convert',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('category_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=255)),
                ('duration', models.PositiveSmallIntegerField()),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sort', models.PositiveIntegerField()),
                ('image_src', models.CharField(max_length=1000)),
                ('content', models.TextField(blank=True, null=True)),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsServiceConsumeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('service_id', models.PositiveIntegerField()),
                ('consume_id', models.PositiveIntegerField()),
                ('consume_type', models.PositiveIntegerField()),
                ('consume_num', models.PositiveIntegerField()),
                ('unit_id', models.IntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_service_consume_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsServiceNotStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('category_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=255)),
                ('duration', models.PositiveSmallIntegerField()),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sort', models.PositiveIntegerField()),
                ('image_src', models.CharField(max_length=100)),
                ('nav_images', models.CharField(max_length=1000)),
                ('create_staff_id', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_service_not_standard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreConsume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('consume_id', models.PositiveIntegerField()),
                ('type', models.PositiveIntegerField()),
                ('store_category_id', models.PositiveIntegerField()),
                ('store_cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_num', models.IntegerField()),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_consume',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreInvestCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('invest_card_id', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_invest_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStorePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('package_id', models.PositiveIntegerField()),
                ('is_standard', models.PositiveIntegerField()),
                ('store_category_id', models.PositiveIntegerField()),
                ('store_origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('store_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_package',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStorePackageLimitBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_package_id', models.PositiveIntegerField()),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('package_id', models.PositiveIntegerField()),
                ('is_standard', models.PositiveIntegerField()),
                ('limit_buy_num', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_package_limit_buy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStorePackageShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_package_id', models.PositiveIntegerField()),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('package_id', models.PositiveIntegerField()),
                ('is_standard', models.PositiveIntegerField()),
                ('is_show', models.PositiveIntegerField()),
                ('app_show', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_package_show',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('store_category_id', models.PositiveIntegerField()),
                ('store_origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('store_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreProductLimitBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_product_id', models.PositiveIntegerField()),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('limit_buy_num', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_product_limit_buy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreProductShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_product_id', models.PositiveIntegerField()),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('is_show', models.PositiveIntegerField()),
                ('app_show', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_product_show',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('service_id', models.PositiveIntegerField()),
                ('is_standard', models.PositiveIntegerField()),
                ('store_category_id', models.PositiveIntegerField()),
                ('store_origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('store_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreServiceLimitBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_service_id', models.PositiveIntegerField()),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('service_id', models.PositiveIntegerField()),
                ('is_standard', models.PositiveIntegerField()),
                ('limit_buy_num', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_service_limit_buy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsStoreServiceShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_service_id', models.PositiveIntegerField()),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('service_id', models.PositiveIntegerField()),
                ('is_standard', models.PositiveIntegerField()),
                ('is_show', models.PositiveIntegerField()),
                ('app_show', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_store_service_show',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('unit', models.CharField(max_length=5)),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'goods_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
                ('staff_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('type', models.PositiveIntegerField()),
                ('remark', models.CharField(max_length=100)),
                ('origin', models.PositiveIntegerField()),
                ('total_origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_sell_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_id', models.PositiveIntegerField()),
                ('coupon_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_pre_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('member_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_should_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_real_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_method', models.PositiveIntegerField()),
                ('is_batch_pay', models.IntegerField()),
                ('order_code', models.IntegerField()),
                ('comment_code', models.IntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('master_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
                ('package_id', models.PositiveIntegerField()),
                ('staff_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=100)),
                ('image_src', models.CharField(max_length=100)),
                ('package_term', models.DateTimeField()),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('scribing_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('member_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_id', models.PositiveIntegerField()),
                ('change_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pre_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('should_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('real_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_method', models.PositiveIntegerField()),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_package',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('master_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
                ('staff_id', models.PositiveIntegerField()),
                ('store_category_id', models.PositiveIntegerField()),
                ('priduct_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('image_src', models.CharField(max_length=100)),
                ('pick_up_code', models.CharField(max_length=30)),
                ('stock_id', models.PositiveIntegerField()),
                ('remark', models.CharField(max_length=100)),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('scribing_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('member_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_id', models.PositiveIntegerField()),
                ('change_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pre_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_should_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('should_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('real_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_method', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderRevestCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('master_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
                ('card_id', models.PositiveIntegerField()),
                ('staff_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('card_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('give_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('give_term', models.DateTimeField()),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('scribing_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_id', models.PositiveIntegerField()),
                ('change_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pre_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('should_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('real_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_method', models.PositiveIntegerField()),
                ('give_used_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('give_over_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_revest_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mch_id', models.PositiveIntegerField()),
                ('store_id', models.PositiveIntegerField()),
                ('master_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField()),
                ('staff_id', models.PositiveIntegerField()),
                ('service_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('image_src', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('scribing_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('member_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_id', models.PositiveIntegerField()),
                ('change_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pre_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('should_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('real_receive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_method', models.PositiveIntegerField()),
                ('state', models.PositiveIntegerField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'order_service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SdkLtv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_type', models.PositiveIntegerField()),
                ('register_time', models.DateField()),
                ('incr_amt', models.PositiveIntegerField()),
                ('day1', models.BigIntegerField()),
                ('day2', models.BigIntegerField()),
                ('day3', models.BigIntegerField()),
                ('day4', models.BigIntegerField()),
                ('day5', models.BigIntegerField()),
                ('day6', models.BigIntegerField()),
                ('day7', models.BigIntegerField()),
                ('day8', models.BigIntegerField()),
                ('day9', models.BigIntegerField()),
                ('day10', models.BigIntegerField()),
                ('day11', models.BigIntegerField()),
                ('day12', models.BigIntegerField()),
                ('day13', models.BigIntegerField()),
                ('day14', models.BigIntegerField()),
                ('day15', models.BigIntegerField()),
                ('day16', models.BigIntegerField()),
                ('day17', models.BigIntegerField()),
                ('day18', models.BigIntegerField()),
                ('day19', models.BigIntegerField()),
                ('day20', models.BigIntegerField()),
                ('day21', models.BigIntegerField()),
                ('day22', models.BigIntegerField()),
                ('day23', models.BigIntegerField()),
                ('day24', models.BigIntegerField()),
                ('day25', models.BigIntegerField()),
                ('day26', models.BigIntegerField()),
                ('day27', models.BigIntegerField()),
                ('day28', models.BigIntegerField()),
                ('day29', models.BigIntegerField()),
                ('day30', models.BigIntegerField()),
                ('count_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'sdk_ltv',
                'managed': False,
            },
        ),
    ]
