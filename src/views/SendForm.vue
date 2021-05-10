<template>
  <div>
    <re-captcha
      :siteKey="recaptcha"
      @verify="verify"
      @expire="expiredCallback"
      @fail="errorCallback"
      @token="receiveToken"
      ref="recaptcha"
    />
    <div>
      <label
        for="Name"
        style="width:100px;display:inline-block;text-align:right;margin-right:2em"
      >
        Name
      </label>
      <input type="text" name="name" id="name" />
    </div>
    <div>
      <label
        for="tel"
        style="width:100px;display:inline-block;text-align:right;margin-right:2em"
      >
        Tel
      </label>
      <input type="tel" name="tel" id="tel" />
    </div>
    <div>
      <label
        for="description"
        style="width:100px;display:inline-block;text-align:right;vertical-align:top;margin-right:2em"
      >
        Description
      </label>
      <textarea name="description" id="description" />
    </div>
    <button
      @click="submit"
    >
      Submit Form
    </button>
    <!-- <button
      @click="getToken"
    >
      Get Token
    </button>
    <div>
      {{ token }}
    </div> -->
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import ReCaptcha from '@/components/ReCaptcha.vue'
import config from '@/config'
import axios from 'axios'
export default Vue.extend({
  name: 'SendForm',
  components: {
    ReCaptcha
  },
  data () {
    return {
      token: '',
      recaptcha: config.recaptcha,
      inputValue: {
        name: '',
        tel: '',
        description: ''
      }
    }
  },
  methods: {
    verify (response: string) {
      console.log(response)
    },
    expiredCallback () {
      console.log('expiredCallback')
    },
    errorCallback (error: any) {
      console.log('errorCallback')
      console.log(error)
    },
    submit () {
      // (this.$refs.recaptcha as any).execute()
      this.getToken()
      if (!this.getToken) {
        this.$root.$emit('recaptcha.invoke')
        this.submit()
      } else {
        const data = {
          ...this.inputValue,
          recaptcha_token: this.token
        }
        console.log(this.$axios)
        // axios.post(config.contractUsApi, data).then((value: any) => {
        //   console.log(value)
        // }).catch((error: any) => {
        //   console.error(error)
        // }).finally(() => {
        //   this.token = ''
        // })
      }
    },
    getToken () {
      // this.token = (this.$refs.recaptcha as any).token()
      // if (!this.token) {
      //   this.token = 'Please challenge once agian'
      // }
      this.$root.$emit('recaptcha.token')
    },
    receiveToken (token: string) {
      this.token = token
      // if (!token) {
      //   this.token = 'Please challenge once agian'
      // }
    }
  }
})
</script>

<style>
</style>
