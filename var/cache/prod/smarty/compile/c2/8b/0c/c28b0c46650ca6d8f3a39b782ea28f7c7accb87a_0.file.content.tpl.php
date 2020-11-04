<?php
/* Smarty version 3.1.33, created on 2020-11-04 18:40:23
  from '/var/www/html/admin984yhuq8x/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5fa2e787202a11_16794712',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'c28b0c46650ca6d8f3a39b782ea28f7c7accb87a' => 
    array (
      0 => '/var/www/html/admin984yhuq8x/themes/default/template/content.tpl',
      1 => 1600952248,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5fa2e787202a11_16794712 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>


<div class="row">
	<div class="col-lg-12">
		<?php if (isset($_smarty_tpl->tpl_vars['content']->value)) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
