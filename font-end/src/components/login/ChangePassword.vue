<template>
		<div class="change-password-layout position-fixed top-0 w-100 h-100">
            <div class="container d-flex flex-column justify-content-center h-100">
                <div class="row d-flex flex-column   bg-white shadow rounded p-3 ">
                    <div class="col my-2 position-relative" >
                        <p class="m-0">Mật khẩu hiện tại:</p>
                        <input v-model="passwordCurent" class="my-2 w-100 border"
						v-blind:class="{ 'border border-danger' : error_empty.passwordCurent == true }"
						:class="{ 'border border-danger' : message != ''}"
						:type="[ show.passwordCurent == true ? 'text' : 'password']"
						>
						<button class="unmask" type="button" title="Mask/Unmask password to check content" @click ="showInforPassword(1)">
							<font-awesome-icon v-if="!show.passwordCurent" icon="fa-solid fa-eye"/>
							<font-awesome-icon v-if="show.passwordCurent" icon="fa-solid fa-eye-slash" />
						</button>
                    </div>
                    <div class="col my-2 position-relative">
                        <p class="m-0">Mật khẩu Mới:</p>
                        <input v-model="passwordNew" class="my-2 w-100 border" 
						:class="{ 'border border-danger' : error_empty.passwordNew == true }" 
						:type="[ show.passwordNew == true ? 'text' : 'password']" >
						<button class="unmask" type="button" title="Mask/Unmask password to check content" @click ="showInforPassword(2)">
							<font-awesome-icon v-if="!show.passwordNew" icon="fa-solid fa-eye"/>
							<font-awesome-icon v-if="show.passwordNew" icon="fa-solid fa-eye-slash" />
						</button>
                    </div>
                    <div class="col my-2 position-relative">
                        <p class="m-0">Nhập lại mật khẩu Mới:</p>
                        <input v-model="passwordNewPermisstion" class="my-2 w-100 border" 
						v-blind:class="{ 'border border-danger' : error_empty.passwordNewPermisstion == true}" 
						:type="[ show.passwordNewPermisstion == true ? 'text' : 'password']" 
						:class="{ 'border border-danger' : password_register_confirm_error== true}"
						v-on:blur="handleBlur" >
						<button class="unmask" type="button" title="Mask/Unmask password to check content" @click ="showInforPassword(3)"
						>
							<font-awesome-icon v-if="!show.passwordNewPermisstion" icon="fa-solid fa-eye"/>
							<font-awesome-icon v-if="show.passwordNewPermisstion" icon="fa-solid fa-eye-slash" />
						</button>
                    </div>
					<div v-if="password_register_confirm_error" class="text-danger">
						Nhập khẩu mới và nhập lại không giống nhau
					</div>
					<div v-if="message != ''" class="text-danger">
						{{message}}
					</div>
                    <div class="col my-2 d-flex align-items-center justify-content-between">
                        <div class="btn btn-dark m-auto" @click="changePassword">
                            Đổi mật khẩu
                        </div>
                        <div class="btn btn-dark m-auto" @click="$emit('hide',false)">
                            Hủy
                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import {actionUser} from './../../common/user.service'
export default {
	name: 'ChangePassword',
	data() {
		return {
			/* ------------------------------ data v-model ------------------------------ */
			passwordCurent : '',
			passwordNew : '',
			passwordNewPermisstion : '' ,
			/* ---------------------------- data notify error --------------------------- */
			password_register_confirm_error : false,
			error_empty: {
				passwordCurent: false,
				passwordNew: false,
				passwordNewPermisstion: false,
			},
			message : '',
			/* -------------------------- data show information ------------------------- */
			show : {
				passwordCurent: false,
				passwordNew: false,
				passwordNewPermisstion: false,
			}
		}	
	},
	methods: {
		/* -------------------------------------------------------------------------- */
		/*                                   ACTIONS                                  */
		/* -------------------------------------------------------------------------- */
		checkData() {
			console.log("check data running")
			if (this.passwordCurent == '') this.error_empty.passwordCurent = true; else this.error_empty.passwordCurent = false;
			if (this.passwordNew == '') this.error_empty.passwordNew = true; else this.error_empty.passwordNew = false;
			if (this.passwordNewPermisstion == '') this.error_empty.passwordNewPermisstion = true; else this.error_empty.passwordNewPermisstion = false;

			if (
				this.error_empty.passwordCurent == true ||
				this.error_empty.passwordNew == true ||
				this.error_empty.passwordNewPermisstion == true
			) {
				return false
			}
			return true
		},
		/* --------------------- check password no same register -------------------- */

		checkPasswordSame() {
			return this.passwordNew == this.passwordNewPermisstion ? true : false
		},
		changePassword(){
			if( this.checkData() == true){
				actionUser.changePassword({
					params : {
						token_permission_infor_user : localStorage.getItem('token_permission_infor_user'),
						password : this.passwordCurent,
						email_user : this.get_user.user ,
						password_new : this.passwordNew
					}
				}).then(res => {
					console.log(res)
					if(res.user != false){
						this.$emit('hide',false)
						this.$store.dispatch('notice/actionTypeNotice',{content : 'Bạn vừa thay đổi mật khẩu thành công',type : 'addtocart'})
						this.$store.dispatch('notice/activateShowMenu')
						localStorage.setItem('token_permission_infor_user',res.user.token_permission_infor_user)
					}else{
						this.message = res.error.value
					}
				})
			}
		},
		showInforPassword(type){
			switch(type) {
				case 1:
					this.show.passwordCurent = ! this.show.passwordCurent;
					break;
				case 2:
					this.show.passwordNew = ! this.show.passwordNew
					break;
				default:
					this.show.passwordNewPermisstion = !this.show.passwordNewPermisstion
					// code block
			}
		},
		/* -------------------------------------------------------------------------- */
		/*                              METHODS HANDLE UI                             */
		/* -------------------------------------------------------------------------- */
		handleBlur() {
			console.log("handleBlur")
			if (this.checkPasswordSame() == false) {
				this.password_register_confirm_error = true
			}
			else {
				this.password_register_confirm_error = false
			}
		}
	},
	computed: {
		...mapGetters('auth', {
			get_user: 'currentUser',
			get_authenticated: 'isAuthenticated',
			get_error: 'errorAuthenticated'
		}),
		...mapActions('auth', {
			login_user: 'login',
			register_user: 'register'
		}),
	},
	mounted() {
		if (this.authenticated == true) {
			this.$router.push("/");
		}
	}

}
</script>
<style lang="scss">
.change-password-layout {
    z-index: 99999;
    display:flex;
    background-color: rgb(145, 137, 127 , 0.5);
}
.change-password-layout .container {
    max-width: 500px !important;
    margin-right: auto;
    margin-left: auto;
    margin-top:auto;
}
.unmask {
	position:absolute;
	top:50%;
	right:5%;
	border:none;
	background-color:transparent;
}
</style>